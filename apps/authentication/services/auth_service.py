from rest_framework.exceptions import ValidationError

from apps.authentication.models import User
from apps.authentication.services.otp_service import OTPService
from apps.authentication.services.sms_service import SMSService
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.models import User
from apps.authentication.services.otp_service import OTPService

class AuthService:
    """
    Authentication business logic.
    """
    @staticmethod
    def send_otp(mobile_number, role):
        try:
            user = User.objects.get(
                mobile_number=mobile_number,
                role=role,
                is_active=True,
            )
         
        except User.DoesNotExist:
            raise ValidationError(
                {
                    "mobile_number": [
                        "User not found or inactive."
                    ]
                }
            )

        otp = OTPService.create_otp(
            mobile_number=user.mobile_number,
            purpose="LOGIN",
        )

        SMSService.send_otp(
            mobile_number=user.mobile_number,
            otp=otp.otp,
        )
        
        return {
            "message": "OTP sent successfully."
        }

    @staticmethod
    def verify_otp(mobile_number, otp, role):
        """
        Verify OTP and generate JWT tokens.
        """

        try:
            user = User.objects.get(
                mobile_number=mobile_number,
                role=role,
                is_active=True,
            )

        except User.DoesNotExist:
            raise ValidationError(
                {
                    "mobile_number": [
                        "User not found or inactive."
                    ]
                }
            )

        OTPService.verify_otp(
            user=user,
            otp=otp,
            purpose="LOGIN",
        )

        refresh = RefreshToken.for_user(user)

        return {
            "message": "Login successful.",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "mobile_number": user.mobile_number,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
            }
        }

    @staticmethod
    def get_profile(user):
        """
        Return logged-in user details.
        """

        return {
            "id": user.id,
            "mobile_number": user.mobile_number,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
        }

    @staticmethod
    def logout(refresh_token):
        """
        Blacklist the refresh token.
        """

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return {
                "message": "Logout successful."
            }

        except Exception:
            raise ValidationError(
                {
                    "refresh": [
                        "Invalid or expired refresh token."
                    ]
                }
            )


    @staticmethod
    def refresh_access_token(refresh_token):
        """
        Generate a new access token using refresh token.
        """

        try:
            refresh = RefreshToken(refresh_token)

            return {
                "message": "Access token refreshed successfully.",
                "access": str(refresh.access_token),
            }

        except Exception:
            raise ValidationError(
                {
                    "refresh": [
                        "Invalid or expired refresh token."
                    ]
                }
            )


    @staticmethod
    def resend_otp(mobile_number, role):
        """
        Resend login OTP.
        """

        try:
            user = User.objects.get(
                mobile_number=mobile_number,
                role=role,
                is_active=True,
            )

        except User.DoesNotExist:
            raise ValidationError(
                {
                    "mobile_number": [
                        "User not found or inactive."
                    ]
                }
            )

        OTPService.check_resend_cooldown(
        user=user,
        purpose="LOGIN",
        )

        OTPService.check_resend_attempts(
        user=user,
        purpose="LOGIN",
        )

        otp = OTPService.create_otp(
            mobile_number=user.mobile_number,
            purpose="LOGIN",
        )

        SMSService.send_otp(
            mobile_number=user.mobile_number,
            otp=otp.otp,
        )

        return {
            "message": "OTP resent successfully."
        }