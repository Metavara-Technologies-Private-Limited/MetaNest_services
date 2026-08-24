from rest_framework import serializers
from apps.administration.models import BillingSetting


class BillingSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingSetting
        fields = [
            'id',
            'receipt_prefix',
            'starting_no',
            'bill_prefix',
            'financial_year',
            'created_at',
            'updated_at',
        ]