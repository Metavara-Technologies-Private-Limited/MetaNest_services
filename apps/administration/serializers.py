from rest_framework import serializers

from apps.authentication.models import User


class AdminUserSerializer(serializers.ModelSerializer):
	phone_number = serializers.CharField(source="mobile_number")
	status = serializers.SerializerMethodField()
	last_login = serializers.DateTimeField(read_only=True)

	class Meta:
		model = User
		fields = (
			"id",
			"first_name",
			"last_name",
			"email",
			"phone_number",
			"role",
			"status",
			"last_login",
		)

	def get_status(self, obj):
		return "Active" if obj.is_active else "Inactive"

	def validate_phone_number(self, value):
		if not value.isdigit() or len(value) != 10:
			raise serializers.ValidationError("Enter a valid 10-digit mobile number.")
		return value

	def create(self, validated_data):
		mobile_number = validated_data.pop("mobile_number")
		return User.objects.create_user(mobile_number=mobile_number, **validated_data)
