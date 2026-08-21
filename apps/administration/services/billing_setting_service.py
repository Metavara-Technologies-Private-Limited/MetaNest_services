from apps.administration.models import BillingSetting


class BillingSettingService:
    @staticmethod
    def get_billing_settings():
        obj, _ = BillingSetting.objects.get_or_create(
            id=1,
            defaults={
                "receipt_prefix": "RCP",
                "starting_no": 2024001,
                "bill_prefix": "BILL",
                "financial_year": "2024-25",
            }
        )
        return obj

    @staticmethod
    def update_billing_settings(data):
        obj = BillingSettingService.get_billing_settings()
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return obj