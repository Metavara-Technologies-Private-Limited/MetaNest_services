from rest_framework import serializers

from apps.people.models import Resident, SecurityStaff


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = [
            "id",
            "name",
            "resident_type",
            "flat",
            "phone",
            "move_in_date",
            "family_members",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class SecurityStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityStaff
        fields = [
            "id",
            "name",
            "role",
            "shift",
            "phone",
            "salary",
            "joining_date",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]