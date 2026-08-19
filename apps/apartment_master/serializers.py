from rest_framework import serializers

from apps.apartment_master import services
from apps.apartment_master.models import Flat, FlatType, Floor, Society, Wing


class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Society
        fields = [
            "id",
            "name",
            "registration_number",
            "address_line1",
            "address_line2",
            "city",
            "state",
            "pincode",
            "contact_email",
            "contact_phone",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at","is_active",]


class SocietySummarySerializer(serializers.Serializer):
    """Read-only serializer for the calculated dashboard summary.
    Not a ModelSerializer since none of these fields are stored."""

    society_id = serializers.IntegerField()
    society_name = serializers.CharField()
    total_wings = serializers.IntegerField()
    total_floors = serializers.IntegerField()
    total_flats = serializers.IntegerField()
    occupied_flats = serializers.IntegerField()
    vacant_flats = serializers.IntegerField()
    occupancy_percentage = serializers.FloatField()


class WingSerializer(serializers.ModelSerializer):
    total_floors = serializers.SerializerMethodField()

    class Meta:
        model = Wing
        fields = [
            "id",
            "society",
            "name",
            "total_floors",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "total_floors",]

    def get_total_floors(self, obj):
        return services.get_wing_total_floors(obj)


class FloorSerializer(serializers.ModelSerializer):
    total_flats = serializers.SerializerMethodField()

    class Meta:
        model = Floor
        fields = [
            "id",
            "wing",
            "floor_number",
            "name",
            "total_flats",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "total_flats",]

    def get_total_flats(self, obj):
        return services.get_floor_total_flats(obj)


class FlatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatType
        fields = ["id", "name", "description", "is_active"]
        read_only_fields = ["id"]


class FlatSerializer(serializers.ModelSerializer):
    flat_type_name = serializers.CharField(source="flat_type.name", read_only=True)
    occupancy_status = serializers.SerializerMethodField()

    class Meta:
        model = Flat
        fields = [
            "id",
            "floor",
            "flat_type",
            "flat_type_name",
            "flat_number",
            "carpet_area_sqft",
            "built_up_area_sqft",
            "facing",
            "occupancy_status",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_occupancy_status(self, obj):
        return services.get_flat_occupancy_status(obj)

    def validate_carpet_area_sqft(self, value):
        if value <= 0:
            raise serializers.ValidationError("Carpet area must be greater than zero.")
        return value
    def validate_built_up_area_sqft(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Built-up area must be greater than zero.")
        return value
    def validate(self, attrs):
        carpet = attrs.get("carpet_area_sqft")
        built_up = attrs.get("built_up_area_sqft")

        if (carpet is not None and built_up is not None and built_up < carpet):
            raise serializers.ValidationError(
            {
                "built_up_area_sqft":
                "Built-up area cannot be smaller than carpet area."
            }
        )

        return attrs