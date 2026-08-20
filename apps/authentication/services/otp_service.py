import secrets

from django.utils import timezone

from apps.authentication.models import OTP, User
from rest_framework.exceptions import ValidationError



class OTPService:
    """
    Service class responsible for OTP generation and verification.
    """

    OTP_EXPIRY_MINUTES = 5
    OTP_RESEND_COOLDOWN = 30
    MAX_RESEND_ATTEMPTS = 5

    @staticmethod
    def generate_otp():
        """
        Generate a random 6-digit OTP.
        """
        return str(secrets.randbelow(900000) + 100000)

    @classmethod
    def check_resend_cooldown(cls, user, purpose):
        """
        Prevent OTP resend within cooldown period.
        """

        latest_otp = (
            OTP.objects.filter(
                user=user,
                purpose=purpose,
            )
            .order_by("-created_at")
            .first()
        )

        if not latest_otp:
            return

        elapsed_seconds = (
            timezone.now() - latest_otp.created_at
        ).total_seconds()

        if elapsed_seconds < cls.OTP_RESEND_COOLDOWN:
            remaining = int(
                cls.OTP_RESEND_COOLDOWN - elapsed_seconds
            )

            raise ValidationError(
                {
                    "otp": [
                        f"Please wait {remaining} seconds before requesting another OTP."
                    ]
                }
            )

    @classmethod
    def check_resend_attempts(cls, user, purpose):
        """
        Limit OTP resend attempts.
        """

        attempts = OTP.objects.filter(
            user=user,
            purpose=purpose,
        ).count()

        if attempts >= cls.MAX_RESEND_ATTEMPTS:
            raise ValidationError(
                {
                    "otp": [
                        "You have exceeded the maximum OTP resend attempts."
                    ]
                }
            )

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