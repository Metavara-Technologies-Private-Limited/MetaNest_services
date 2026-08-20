from apps.administration.models import BankAccount


class BankAccountService:
    @staticmethod
    def get_primary_bank_account():
        obj, _ = BankAccount.objects.get_or_create(
            is_primary=True,
            defaults={
                "bank_name": "HDFC Bank, Baner Branch",
                "account_number": "50200067281234",
                "ifsc_code": "HDFC0001234",
                "account_type": "Current Account",
                "is_primary": True,
            }
        )
        return obj

    @staticmethod
    def update_bank_account(data):
        obj = BankAccountService.get_primary_bank_account()
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return obj