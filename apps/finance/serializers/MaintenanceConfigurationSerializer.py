from rest_framework import serializers

from apps.finance.models.MaintenanceConfiguration import MaintenanceConfiguration


class MaintenanceConfigurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceConfiguration
        fields = [
            "id",
            "base_charge",
            "per_sqft_charge",
            "water_charge",
            "parking_charge",
            "sinking_fund",
            "other_charge",
            "due_day",
            "grace_period_days",
            "late_fee_per_day",
            "maximum_late_fee",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]