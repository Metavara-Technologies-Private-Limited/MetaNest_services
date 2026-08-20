from rest_framework import serializers
from apps.administration.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
            'id',
            'bank_name',
            'account_number',
            'ifsc_code',
            'account_type',
            'is_primary',
            'created_at',
            'updated_at',
        ]