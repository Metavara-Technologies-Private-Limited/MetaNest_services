from django.db import models


class Resident(models.Model):

    RESIDENT_TYPE_CHOICES = [
        ("Owner", "Owner"),
        ("Tenant", "Tenant"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    name = models.CharField(max_length=100)

    resident_type = models.CharField(
        max_length=20,
        choices=RESIDENT_TYPE_CHOICES
    )

    flat = models.ForeignKey(
        "apartment_master.Flat",
        on_delete=models.PROTECT,
        related_name="residents"
    )

    phone = models.CharField(max_length=15)

    move_in_date = models.DateField()

    family_members = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name