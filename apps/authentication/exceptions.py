from rest_framework.exceptions import APIException
from rest_framework import status


class AuthenticationException(APIException):
    """
    Base Authentication Exception.
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Authentication error."
    default_code = "authentication_error"


class UserNotFoundException(AuthenticationException):
    """
    Raised when user is not found.
    """

    default_detail = "User not found."
    default_code = "user_not_found"


class InvalidOTPException(AuthenticationException):
    """
    Raised when OTP is invalid.
    """

    default_detail = "Invalid OTP."
    default_code = "invalid_otp"


class OTPExpiredException(AuthenticationException):
    """
    Raised when OTP is expired.
    """

    default_detail = "OTP has expired."
    default_code = "otp_expired"