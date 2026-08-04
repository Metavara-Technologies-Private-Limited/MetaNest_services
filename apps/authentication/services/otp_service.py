import secrets

from django.utils import timezone

from apps.authentication.models import OTP, User
from rest_framework.exceptions import ValidationError


class OTPService:
    """
    Service class responsible for OTP generation and verification.
    """

    OTP_EXPIRY_MINUTES = 5

    @staticmethod
    def generate_otp():
        """
        Generate a random 6-digit OTP.
        """
        return str(secrets.randbelow(900000) + 100000)

    @classmethod
    def create_otp(cls, mobile_number, purpose):
        """
        Create a new OTP for the given user.
        """

        user = User.objects.get(mobile_number=mobile_number)

        # Mark previous OTPs as expired/used
        OTP.objects.filter(
            user=user,
            purpose=purpose,
            is_verified=False
        ).update(is_verified=True)

        otp = cls.generate_otp()

        otp_instance = OTP.objects.create(
            user=user,
            otp=otp,
            purpose=purpose,
            expires_at=timezone.now() + timezone.timedelta(minutes=cls.OTP_EXPIRY_MINUTES)
        )

        return otp_instance


    @staticmethod
    def verify_otp(user, otp, purpose):
        """
        Verify OTP for the given user.
        """

        otp_instance = (
            OTP.objects.filter(
                user=user,
                purpose=purpose,
                is_verified=False,
            )
            .order_by("-created_at")
            .first()
        )

        if not otp_instance:
            raise ValidationError(
                {
                    "otp": [
                        "OTP not found."
                    ]
                }
            )

        if otp_instance.expires_at < timezone.now():
            raise ValidationError(
                {
                    "otp": [
                        "OTP has expired."
                    ]
                }
            )

        if otp_instance.otp != otp:
            raise ValidationError(
                {
                    "otp": [
                        "Invalid OTP."
                    ]
                }
            )

        otp_instance.is_verified = True
        otp_instance.save(update_fields=["is_verified"])

        return True