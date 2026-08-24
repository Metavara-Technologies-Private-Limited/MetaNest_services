import uuid
from django.core.validators import MinValueValidator
from django.db import models

from apps.finance.models.Bill import Bill


class Payment(models.Model):

    PAYMENT_MODE_ONLINE = "ONLINE"
    PAYMENT_MODE_CASH = "CASH"
    PAYMENT_MODE_UPI = "UPI"
    PAYMENT_MODE_NEFT = "NEFT"
    PAYMENT_MODE_CHEQUE = "CHEQUE"

    PAYMENT_MODE_CHOICES = [
        (PAYMENT_MODE_ONLINE, "Online"),
        (PAYMENT_MODE_CASH, "Cash"),
        (PAYMENT_MODE_UPI, "UPI"),
        (PAYMENT_MODE_NEFT, "NEFT"),
        (PAYMENT_MODE_CHEQUE, "Cheque"),
    ]

    PAYMENT_STATUS_SUCCESS = "SUCCESS"
    PAYMENT_STATUS_FAILED = "FAILED"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_SUCCESS, "Success"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    bill = models.ForeignKey(
        Bill,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    receipt_number = models.CharField(
        max_length=50,
        unique=True
    )

    amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    validators=[
        MinValueValidator(0.01)
        ]
    )

    payment_date = models.DateField()

    payment_mode = models.CharField(
        max_length=20,
        choices=PAYMENT_MODE_CHOICES
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_SUCCESS
    )

    transaction_reference = models.CharField(
        max_length=100,
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