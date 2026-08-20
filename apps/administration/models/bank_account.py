from django.db import models


class BankAccount(models.Model):
    bank_name = models.CharField(max_length=200, default="HDFC Bank, Baner Branch")
    account_number = models.CharField(max_length=50, unique=True, default="50200067281234")
    ifsc_code = models.CharField(max_length=20, default="HDFC0001234")
    account_type = models.CharField(max_length=50, default="Current Account")
    is_primary = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"