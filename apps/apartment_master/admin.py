# Register your models here.
from django.contrib import admin

from apps.apartment_master.models import Flat, FlatType, Floor, Society, Wing


class SoftDeleteAdminMixin:
    """Shows soft-deleted rows in admin (using all_objects) instead of
    hiding them entirely, since admins need to review/restore deleted data."""

    def get_queryset(self, request):
        qs = self.model.all_objects.get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


@admin.register(Society)
class SocietyAdmin(SoftDeleteAdminMixin, admin.ModelAdmin):
    list_display = ("name", "registration_number", "city", "is_active", "is_deleted")
    search_fields = ("name", "registration_number", "city")
    list_filter = ("is_active", "is_deleted", "state")
    ordering = ("name",)


@admin.register(Wing)
class WingAdmin(SoftDeleteAdminMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "society",
        "is_active",
        "is_deleted",
    )

    search_fields = (
        "name",
        "society__name",
    )

    list_filter = (
        "society",
        "is_active",
        "is_deleted",
    )

    autocomplete_fields = ("society",)
    ordering = (
    "society",
    "name",
)


@admin.register(Floor)
class FloorAdmin(SoftDeleteAdminMixin, admin.ModelAdmin):
    list_display = ("__str__", "wing", "floor_number", "is_active", "is_deleted")
    search_fields = ("name", "wing__name")
    list_filter = ("is_active", "is_deleted", "wing")
    autocomplete_fields = ("wing",)
    ordering = (
    "wing",
    "floor_number",
)


@admin.register(FlatType)
class FlatTypeAdmin(SoftDeleteAdminMixin, admin.ModelAdmin):
    list_display = ("name", "is_active", "is_deleted")
    search_fields = ("name",)
    list_filter = ("is_active", "is_deleted")
    ordering = ("name",)


@admin.register(Flat)
class FlatAdmin(SoftDeleteAdminMixin, admin.ModelAdmin):
    @admin.display(ordering="floor__wing", description="Wing")
    def wing(self, obj):
        return obj.floor.wing.name

    @admin.display(ordering="floor__wing__society", description="Society")
    def society(self, obj):
        return obj.floor.wing.society.name
    list_display = (
    "flat_number",
    "wing",
    "society",
    "flat_type",
    "carpet_area_sqft",
    "facing",
    "is_active",
    "is_deleted",
)
    search_fields = ("flat_number","floor__wing__name","floor__wing__society__name","flat_type__name",)
    list_filter = ("is_active", "is_deleted", "flat_type", "facing")
    autocomplete_fields = ("floor", "flat_type")