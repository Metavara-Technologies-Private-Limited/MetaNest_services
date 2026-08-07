from drf_spectacular.utils import OpenApiExample


# ============================
# SEND OTP
# ============================

SEND_OTP_REQUEST = OpenApiExample(
    name="Send OTP Request",
    summary="Valid Request",
    request_only=True,
    value={
        "mobile_number": "6361772998",
        "role": "ADMIN"
    },
)

SEND_OTP_SUCCESS = OpenApiExample(
    name="Success Response",
    summary="OTP Sent Successfully",
    response_only=True,
    status_codes=["200"],
    value={
        "success": True,
        "message": "OTP sent successfully."
    },
)

SEND_OTP_USER_NOT_FOUND = OpenApiExample(
    name="User Not Found",
    summary="Invalid User",
    response_only=True,
    status_codes=["400"],
    value={
        "mobile_number": [
            "User not found or inactive."
        ]
    },
)


# ============================
# VERIFY OTP
# ============================

VERIFY_OTP_REQUEST = OpenApiExample(
    name="Verify OTP Request",
    summary="Valid OTP",
    request_only=True,
    value={
        "mobile_number": "6361772998",
        "otp": "123456",
        "role": "ADMIN",
    },
)

VERIFY_OTP_SUCCESS = OpenApiExample(
    name="Login Successful",
    summary="JWT Tokens Returned",
    response_only=True,
    status_codes=["200"],
    value={
        "success": True,
        "message": "Login successful.",
        "data": {
            "access": "eyJhbGciOiJIUzI1NiIs...",
            "refresh": "eyJhbGciOiJIUzI1NiIs...",
            "user": {
                "id": 1,
                "mobile_number": "6361772998",
                "first_name": "Admin",
                "last_name": "User",
                "role": "ADMIN",
            },
        },
    },
)

VERIFY_OTP_INVALID = OpenApiExample(
    name="Invalid OTP",
    summary="Wrong OTP",
    response_only=True,
    status_codes=["400"],
    value={
        "otp": [
            "Invalid OTP."
        ]
    },
)

VERIFY_OTP_EXPIRED = OpenApiExample(
    name="OTP Expired",
    summary="Expired OTP",
    response_only=True,
    status_codes=["400"],
    value={
        "otp": [
            "OTP has expired."
        ]
    },
)

from drf_spectacular.utils import OpenApiExample

RESEND_OTP_REQUEST = OpenApiExample(
    name="Resend OTP",
    summary="Resend OTP Request",
    value={
        "mobile_number": "6361772998",
        "role": "ADMIN"
    },
    request_only=True,
)

RESEND_OTP_SUCCESS = OpenApiExample(
    name="OTP Resent",
    summary="Success Response",
    value={
        "success": True,
        "message": "OTP resent successfully."
    },
    response_only=True,
    status_codes=["200"],
)

RESEND_OTP_USER_NOT_FOUND = OpenApiExample(
    name="User Not Found",
    summary="Error Response",
    value={
        "mobile_number": [
            "User not found or inactive."
        ]
    },
    response_only=True,
    status_codes=["400"],
)

# ============================
# PROFILE
# ============================

PROFILE_SUCCESS = OpenApiExample(
    name="Profile Success",
    summary="Logged-in User Profile",
    response_only=True,
    status_codes=["200"],
    value={
        "success": True,
        "message": "Profile fetched successfully.",
        "data": {
            "id": 1,
            "mobile_number": "6361772998",
            "first_name": "Admin",
            "last_name": "User",
            "role": "ADMIN"
        }
    },
)

PROFILE_UNAUTHORIZED = OpenApiExample(
    name="Unauthorized",
    summary="JWT Token Missing or Invalid",
    response_only=True,
    status_codes=["401"],
    value={
        "detail": "Authentication credentials were not provided."
    },
)

# ============================
# LOGOUT
# ============================

LOGOUT_REQUEST = OpenApiExample(
    name="Logout Request",
    summary="Logout",
    request_only=True,
    value={
        "refresh": "your_refresh_token_here"
    },
)

LOGOUT_SUCCESS = OpenApiExample(
    name="Logout Success",
    summary="Success Response",
    response_only=True,
    status_codes=["200"],
    value={
        "success": True,
        "message": "Logout successful."
    },
)

LOGOUT_UNAUTHORIZED = OpenApiExample(
    name="Unauthorized",
    summary="Invalid Access Token",
    response_only=True,
    status_codes=["401"],
    value={
        "detail": "Authentication credentials were not provided."
    },
)

# ============================
# TOKEN REFRESH
# ============================

TOKEN_REFRESH_REQUEST = OpenApiExample(
    name="Refresh Token",
    summary="Refresh Access Token",
    request_only=True,
    value={
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    },
)

TOKEN_REFRESH_SUCCESS = OpenApiExample(
    name="Token Refreshed",
    summary="Success Response",
    response_only=True,
    status_codes=["200"],
    value={
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    },
)

TOKEN_REFRESH_INVALID = OpenApiExample(
    name="Invalid Refresh Token",
    summary="Invalid Token",
    response_only=True,
    status_codes=["401"],
    value={
        "detail": "Token is invalid or expired.",
        "code": "token_not_valid"
    },
)