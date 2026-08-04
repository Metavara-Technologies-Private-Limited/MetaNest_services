from rest_framework import serializers


class VerifyOTPSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(
        max_length=10,
        min_length=10,
        required=True,
        help_text="Enter 10-digit mobile number."
    )

    otp = serializers.CharField(
        max_length=6,
        min_length=6,
        required=True,
        help_text="Enter 6-digit OTP."
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

        return value

    def validate_otp(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "OTP must contain only digits."
            )

        if len(value) != 6:
            raise serializers.ValidationError(
                "OTP must be exactly 6 digits."
            )

        return value