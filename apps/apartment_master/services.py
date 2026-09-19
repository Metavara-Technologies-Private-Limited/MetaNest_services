"""
All business logic for Apartment Master lives here. Views must stay thin
and only call into these functions — no querysets or business rules in
views.py.
"""
from django.db import transaction

from apps.apartment_master.models import Flat, Floor, Society, Wing


# ---------------------------------------------------------------------------
# Society
# ---------------------------------------------------------------------------

def get_society_summary(society: Society) -> dict:
    """
    Aggregate, always-calculated society-level numbers. Nothing here is
    ever persisted to the DB, per decision #7 — these change constantly
    as flats/wings are added and must never drift out of sync with reality.
    """
    wings = society.wings.filter(is_deleted=False)
    total_wings = wings.count()
    total_floors = Floor.objects.filter(wing__society=society, is_deleted=False).count()
    total_flats = Flat.objects.filter(
        floor__wing__society=society, is_deleted=False
    ).count()

    occupied_flats = get_occupied_flats_count(society)
    occupancy_percentage = (
        round((occupied_flats / total_flats) * 100, 2) if total_flats else 0.0
    )

    return {
        "society_id": society.id,
        "society_name": society.name,
        "total_wings": total_wings,
        "total_floors": total_floors,
        "total_flats": total_flats,
        "occupied_flats": occupied_flats,
        "vacant_flats": total_flats - occupied_flats,
        "occupancy_percentage": occupancy_percentage,
    }


def get_occupied_flats_count(society: Society) -> int:
    """
    A flat is occupied when it has at least one active resident. Distinct
    flat IDs prevent multiple residents in one home from inflating the count.
    """
    from apps.people.models import Resident

    return Resident.objects.filter(
        flat__floor__wing__society=society,
        status="Active",
    ).values("flat_id").distinct().count()


# ---------------------------------------------------------------------------
# Wing
# ---------------------------------------------------------------------------

def get_wing_total_floors(wing: Wing) -> int:
    return wing.floors.filter(is_deleted=False).count()


def create_wing(society: Society, name: str) -> Wing:
    return Wing.objects.create(
        society=society,
        name=name,
    )

# ---------------------------------------------------------------------------
# Floor
# ---------------------------------------------------------------------------

def get_floor_total_flats(floor: Floor) -> int:
    return floor.flats.filter(is_deleted=False).count()


def create_floor(wing: Wing, floor_number: int, name: str = "") -> Floor:
    return Floor.objects.create(wing=wing, floor_number=floor_number, name=name)


# ---------------------------------------------------------------------------
# Flat
# ---------------------------------------------------------------------------

def create_flat(
    floor: Floor,
    flat_type_id: int,
    flat_number: str,
    carpet_area_sqft,
    built_up_area_sqft=None,
    facing: str = "",
) -> Flat:
    return Flat.objects.create(
        floor=floor,
        flat_type_id=flat_type_id,
        flat_number=flat_number,
        carpet_area_sqft=carpet_area_sqft,
        built_up_area_sqft=built_up_area_sqft,
        facing=facing,
    )


def get_flat_occupancy_status(flat: Flat) -> str:
    """
    A flat with at least one active resident is occupied; otherwise it is
    vacant. This keeps the status aligned with society and wing totals.
    """
    from apps.people.models import Resident

    if flat.occupancy_status == Flat.OccupancyStatus.OCCUPIED:
        return "occupied"
    return "occupied" if Resident.objects.filter(flat=flat, status="Active").exists() else "vacant"


from typing import Any
@transaction.atomic
def bulk_create_flats_for_floor(
    floor: Floor,
    flat_specs: list[dict[str, Any]],
) -> list[Flat]:
    """
    Convenience for onboarding an entire floor at once, e.g. from a
    society's existing flat register during initial data migration.
    Each dict in flat_specs should match create_flat's kwargs.
    """
    created = []
    for spec in flat_specs:
        created.append(create_flat(floor=floor, **spec))
    return created


# ---------------------------------------------------------------------------
# Soft delete helpers (cascading down the hierarchy)
# ---------------------------------------------------------------------------

def soft_delete_wing_cascade(wing: Wing) -> None:
    """
    Soft-deletes a Wing and everything beneath it. We do this explicitly
    (rather than relying on on_delete behaviour) because on_delete=PROTECT
    is used throughout this module intentionally — hard deletes should
    never silently cascade in a financial/residential system.
    """
    for floor in wing.floors.filter(is_deleted=False):
        for flat in floor.flats.filter(is_deleted=False):
            flat.delete()
        floor.delete()
    wing.delete()