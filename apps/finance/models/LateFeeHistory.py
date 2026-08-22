import uuid
from django.core.validators import MinValueValidator
from django.db import models

from apps.finance.models.Bill import Bill


class LateFeeHistory(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    bill = models.ForeignKey(
        Bill,
        on_delete=models.PROTECT,
        related_name="late_fee_history"
    )

    principal_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    late_fee_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    waived_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[
        MinValueValidator(0)
        ]
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    waiver_reason = models.TextField(
        null=True,
        blank=True
    )

    waived_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_deleted = models.BooleanField(
        default=False
    )