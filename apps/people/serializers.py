from rest_framework import serializers

from .models import SecurityStaff
from .models import Resident


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

	def validate_phone(self, value):
		digits = "".join(character for character in value if character.isdigit())
		if len(digits) != 10:
			raise serializers.ValidationError("Enter a valid 10-digit mobile number.")
		return digits


class ResidentSerializer(serializers.ModelSerializer):
	flat_number = serializers.CharField(source="flat.flat_number", read_only=True)

	class Meta:
		model = Resident
		fields = [
			"id",
			"name",
			"resident_type",
			"flat",
			"flat_number",
			"phone",
			"email",
			"move_in_date",
			"family_members",
			"status",
			"created_at",
			"updated_at",
		]
		read_only_fields = ["id", "flat_number", "created_at", "updated_at"]

	def validate_phone(self, value):
		digits = "".join(character for character in value if character.isdigit())
		if len(digits) != 10:
			raise serializers.ValidationError("Enter a valid 10-digit mobile number.")
		return digits
