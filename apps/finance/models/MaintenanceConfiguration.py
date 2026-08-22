import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class MaintenanceConfiguration(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # Monthly Charges
    base_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    per_sqft_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    water_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    parking_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    sinking_fund = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    other_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # Due Date & Late Fee
    due_day = models.PositiveSmallIntegerField(
    validators=[
        MinValueValidator(1),
        MaxValueValidator(31),
        ]
    )

    grace_period_days = models.PositiveIntegerField(
        default=0
    )

    late_fee_per_day = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    maximum_late_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # Common fields
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_deleted = models.BooleanField(
        default=False
    )