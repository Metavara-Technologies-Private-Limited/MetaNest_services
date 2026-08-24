from rest_framework import serializers

from apps.finance.models.LateFeeHistory import LateFeeHistory


class LateFeeHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LateFeeHistory
        fields = [
            "id",
            "bill",
            "principal_amount",
            "late_fee_amount",
            "waived_amount",
            "total_amount",
            "waiver_reason",
            "waived_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "principal_amount",
            "late_fee_amount",
            "waived_amount",
            "total_amount",
            "waiver_reason",
            "waived_at",
            "created_at",
            "updated_at",
        ]