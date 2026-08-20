from django.db import models


class BillingSetting(models.Model):
    receipt_prefix = models.CharField(max_length=10, default="RCP")
    starting_no = models.PositiveIntegerField(default=2024001)
    bill_prefix = models.CharField(max_length=10, default="BILL")
    financial_year = models.CharField(max_length=20, default="2024-25")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Billing Config ({self.financial_year})"