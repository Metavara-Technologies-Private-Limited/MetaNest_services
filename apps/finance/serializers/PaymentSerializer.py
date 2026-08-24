from rest_framework import serializers

from apps.finance.models.Payment import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = [
            "id",
            "bill",
            "receipt_number",
            "amount",
            "payment_date",
            "payment_mode",
            "payment_status",
            "transaction_reference",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "receipt_number",
            "payment_status",
            "created_at",
            "updated_at",
        ]