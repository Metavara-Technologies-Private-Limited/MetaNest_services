from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class ActiveManager(models.Manager):
    """
    Default manager: hides soft-deleted rows everywhere by default.
    This is deliberate — 90% of the app should never see deleted rows
    without asking for them explicitly.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class AllObjectsManager(models.Manager):
    """Unfiltered manager — used by Django Admin and audit/reporting tools
    that need to see soft-deleted rows too."""

    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    """
    Abstract base providing audit + soft-delete fields for every model in
    this app.

    NOTE: This intentionally lives here rather than in a shared `apps.common`
    app. Other apps (people, finance, ...) will likely want the identical
    fields, but introducing a new shared app is a team-wide architecture
    decision, not something to bake in unilaterally two weeks into a
    15-person project. When the team agrees to standardize, this class can
    be lifted into apps/common/models.py verbatim with no changes needed —
    it has no dependency on anything else in this file.

    is_active: whether the record is currently in active use
               (e.g. a Wing under renovation could be marked inactive
               without being "deleted").
    is_deleted: soft-delete flag. Real DB rows are never removed;
                `delete()` is overridden to flip this flag instead.
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="Deleted At")

    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False, hard=False):
        """
        Soft delete by default. Pass hard=True to actually remove the row
        (should only ever be used from admin scripts / data cleanup, never
        from application code paths).
        """
        if hard:
            return super().delete(using=using, keep_parents=keep_parents)
        self.is_deleted = True
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save(update_fields=["is_deleted", "is_active", "deleted_at"])

    def restore(self):
        self.is_deleted = False
        self.is_active = True
        self.deleted_at = None
        self.save(update_fields=["is_deleted", "is_active", "deleted_at"])


class Society(BaseModel):
    """
    Root of the spatial hierarchy. Current MVP manages exactly one Society,
    but this is modeled as a real table (not hardcoded) so that migrating
    to multi-tenant later doesn't require a destructive schema rewrite.
    """

    name = models.CharField(max_length=255, verbose_name="Society Name")
    registration_number = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Registration Number",
        help_text="Society/RERA registration number",
    )
    address_line1 = models.CharField(max_length=255, verbose_name="Address Line 1")
    address_line2 = models.CharField(max_length=255, blank=True, verbose_name="Address Line 2")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name = "Society"
        verbose_name_plural = "Societies"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Wing(BaseModel):
    """
    Represents a physical wing/block/tower within a society.

    Examples:
        A
        B
        C

    The UI is responsible for displaying these as
    "Wing A", "Wing B", etc., avoiding duplicate
    storage of both name and code.
    """

    society = models.ForeignKey(
        Society,
        on_delete=models.PROTECT,
        related_name="wings",
        verbose_name="Society",
    )

    name = models.CharField(
        max_length=50,
        verbose_name="Wing",
        help_text="Unique wing identifier (e.g. A, B, C).",
    )

    class Meta:
        verbose_name = "Wing"
        verbose_name_plural = "Wings"
        ordering = ["society", "name"]

        constraints = [
            models.UniqueConstraint(
                fields=["society", "name"],
                name="uniq_wing_name_per_society",
            ),
        ]

        indexes = [
            models.Index(
                fields=["society", "name"],
                name="idx_wing_society_name",
            ),
        ]

    def __str__(self):
        return f"{self.society.name} - Wing {self.name}"


class Floor(BaseModel):
    """A floor within a Wing. floor_number is signed to allow basements."""

    wing = models.ForeignKey(
        Wing,
        on_delete=models.PROTECT,
        related_name="floors",
        verbose_name="Wing",
    )
    floor_number = models.SmallIntegerField(
        verbose_name="Floor Number",
        help_text="0 = Ground floor. Negative values represent basements.",
    )
    name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Floor Name",
        help_text="Optional human label, e.g. 'Ground', 'Mezzanine'",
    )

    class Meta:
        verbose_name = "Floor"
        verbose_name_plural = "Floors"
        ordering = ["wing", "floor_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["wing", "floor_number"], name="uniq_floor_number_per_wing"
            ),
        ]
        indexes = [
            models.Index(fields=["wing", "floor_number"], name="idx_floor_wing_number"),
        ]

    def __str__(self):
        return self.name or f"{self.wing} - Floor {self.floor_number}"


class FlatType(BaseModel):
    """
    Master table for configurable flat types such as
    1BHK, 2BHK, 3BHK, Studio, Duplex, etc.
    """

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Flat Type",
        help_text="Examples: 1BHK, 2BHK, Studio, Duplex",
    )

    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Flat Type"
        verbose_name_plural = "Flat Types"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Flat(BaseModel):
    """
    Leaf node of the spatial hierarchy. This is the anchor that People,
    Finance, Visitors, Maintenance, and Analytics modules will all attach
    to via foreign keys in their own apps.

    Deliberately excludes: owner/tenant identity, occupancy status,
    maintenance amount. Those are derived or belong to other modules.
    """

    class Facing(models.TextChoices):
        NORTH = "N", "North"
        SOUTH = "S", "South"
        EAST = "E", "East"
        WEST = "W", "West"
        NORTH_EAST = "NE", "North-East"
        NORTH_WEST = "NW", "North-West"
        SOUTH_EAST = "SE", "South-East"
        SOUTH_WEST = "SW", "South-West"

    floor = models.ForeignKey(
        Floor,
        on_delete=models.PROTECT,
        related_name="flats",
        verbose_name="Floor",
    )
    flat_type = models.ForeignKey(
        FlatType,
        on_delete=models.PROTECT,
        related_name="flats",
        verbose_name="Flat Type",
    )
    flat_number = models.CharField(
        max_length=20,
        verbose_name="Flat Number",
        help_text="e.g. '101', '101-A'",
    )
    carpet_area_sqft = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Carpet Area (sqft)",
    )
    built_up_area_sqft = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0.01)],
        verbose_name="Built-up Area (sqft)",
    )
    facing = models.CharField(
        max_length=2,
        choices=Facing.choices,
        blank=True,
        verbose_name="Facing",
    )

    class Meta:
        verbose_name = "Flat"
        verbose_name_plural = "Flats"
        ordering = ["floor", "flat_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["floor", "flat_number"], name="uniq_flat_number_per_floor"
            ),
            models.CheckConstraint(
                condition=models.Q(carpet_area_sqft__gt=0),
                name="chk_flat_carpet_area_positive",
            ),
        ]
        indexes = [
            models.Index(fields=["floor", "flat_number"], name="idx_flat_floor_number"),
            models.Index(fields=["flat_number"], name="idx_flat_number"),
        ]

    def __str__(self):
        return f"Wing {self.floor.wing.name} - Flat {self.flat_number}"