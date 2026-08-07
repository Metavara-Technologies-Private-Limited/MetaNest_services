from rest_framework import serializers


class SendOTPSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(
        max_length=10,
        min_length=10,
        required=True,
        help_text="Enter 10-digit mobile number."
    )

    role = serializers.ChoiceField(
        choices=[
            ("ADMIN", "Admin"),
            ("RESIDENT", "Resident"),
        ],
        required=True,
    )

    def validate_mobile_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Mobile number must contain only digits."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Mobile number must be exactly 10 digits."
            )

        return value