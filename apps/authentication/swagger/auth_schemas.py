from drf_spectacular.utils import OpenApiResponse
from apps.authentication.swagger.auth_serializers import (
    SendOTPResponseSerializer,
    VerifyOTPResponseSerializer,
    ResendOTPResponseSerializer,
    ProfileResponseSerializer,
    LogoutResponseSerializer,
)


# ============================
# SEND OTP
# ============================

SEND_OTP_RESPONSE = OpenApiResponse(
    response=SendOTPResponseSerializer,
    description="OTP sent successfully."
)

SEND_OTP_BAD_REQUEST = OpenApiResponse(
    description="Validation Error"
)


# ============================
# VERIFY OTP
# ============================

VERIFY_OTP_RESPONSE = OpenApiResponse(
    response=VerifyOTPResponseSerializer,
    description="Login successful.",
)

VERIFY_OTP_BAD_REQUEST = OpenApiResponse(
    description="Invalid or expired OTP."
)


RESEND_OTP_RESPONSE = OpenApiResponse(
    response=ResendOTPResponseSerializer,
    description="OTP resent successfully.",
)

RESEND_OTP_BAD_REQUEST = OpenApiResponse(
    description="User not found or inactive.",
)

# ============================
# PROFILE
# ============================

PROFILE_RESPONSE = OpenApiResponse(
    response=ProfileResponseSerializer,
    description="Profile fetched successfully.",
)

PROFILE_UNAUTHORIZED_RESPONSE = OpenApiResponse(
    description="Authentication credentials were not provided.",
)

# ============================
# LOGOUT
# ============================

LOGOUT_RESPONSE = OpenApiResponse(
    response=LogoutResponseSerializer,
    description="Logout successful.",
)

LOGOUT_UNAUTHORIZED_RESPONSE = OpenApiResponse(
    description="Authentication credentials were not provided.",
)