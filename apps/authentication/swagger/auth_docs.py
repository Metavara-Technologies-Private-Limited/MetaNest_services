from apps.authentication.swagger.auth_tags import AUTHENTICATION_TAG
from apps.authentication.serializers.otp_serializer import SendOTPSerializer
from apps.authentication.serializers.auth_serializer import VerifyOTPSerializer
from apps.authentication.serializers.resend_otp_serializer import ResendOTPSerializer
from apps.authentication.serializers.logout_serializer import LogoutSerializer

from apps.authentication.swagger.auth_examples import (
    SEND_OTP_REQUEST,
    SEND_OTP_SUCCESS,
    SEND_OTP_USER_NOT_FOUND,
    RESEND_OTP_REQUEST,
    RESEND_OTP_SUCCESS,
    RESEND_OTP_USER_NOT_FOUND,
    VERIFY_OTP_REQUEST,
    VERIFY_OTP_SUCCESS,
    VERIFY_OTP_INVALID,
    VERIFY_OTP_EXPIRED,
    VERIFY_OTP_SUCCESS,
    VERIFY_OTP_INVALID,
    VERIFY_OTP_EXPIRED,
    PROFILE_SUCCESS,
    PROFILE_UNAUTHORIZED,
    LOGOUT_REQUEST,
    LOGOUT_SUCCESS,
    LOGOUT_UNAUTHORIZED,
)

from apps.authentication.swagger.auth_schemas import (
    SEND_OTP_RESPONSE,
    SEND_OTP_BAD_REQUEST,
    RESEND_OTP_RESPONSE,
    RESEND_OTP_BAD_REQUEST,
    VERIFY_OTP_RESPONSE,
    VERIFY_OTP_BAD_REQUEST,
    PROFILE_RESPONSE,
    PROFILE_UNAUTHORIZED_RESPONSE,
    LOGOUT_RESPONSE,
    LOGOUT_UNAUTHORIZED_RESPONSE,
)


SEND_OTP_DOCS = {
    "tags": [AUTHENTICATION_TAG],
    "summary": "Send Login OTP",
    "description": "Generate and send OTP to the registered mobile number.",
    "request": SendOTPSerializer,
    "responses": {
        200: SEND_OTP_RESPONSE,
        400: SEND_OTP_BAD_REQUEST,
    },
    "examples": [
        SEND_OTP_REQUEST,
        SEND_OTP_SUCCESS,
        SEND_OTP_USER_NOT_FOUND,
    ],
}


VERIFY_OTP_DOCS = {
    "tags": [AUTHENTICATION_TAG],
    "summary": "Verify Login OTP",
    "description": "Verify OTP and login user.",
    "request": VerifyOTPSerializer,
    "responses": {
        200: VERIFY_OTP_RESPONSE,
        400: VERIFY_OTP_BAD_REQUEST,
    },
    "examples": [
        VERIFY_OTP_REQUEST,
        VERIFY_OTP_SUCCESS,
        VERIFY_OTP_INVALID,
        VERIFY_OTP_EXPIRED,
    ],
}


RESEND_OTP_DOCS = {
    "tags": [AUTHENTICATION_TAG],
    "summary": "Resend Login OTP",
    "description": "Resend OTP to the registered mobile number.",
    "request": ResendOTPSerializer,
    "responses": {
        200: RESEND_OTP_RESPONSE,
        400: RESEND_OTP_BAD_REQUEST,
    },
    "examples": [
        RESEND_OTP_REQUEST,
        RESEND_OTP_SUCCESS,
        RESEND_OTP_USER_NOT_FOUND,
    ],
}

PROFILE_DOCS = {
    "tags": [AUTHENTICATION_TAG],
    "summary": "Get User Profile",
    "description": "Fetch the profile of the authenticated user.",
    "responses": {
        200: PROFILE_RESPONSE,
        401: PROFILE_UNAUTHORIZED_RESPONSE,
    },
    "examples": [
        PROFILE_SUCCESS,
        PROFILE_UNAUTHORIZED,
    ],
}

LOGOUT_DOCS = {
    "tags": [AUTHENTICATION_TAG],
    "summary": "Logout",
    "description": "Logout the authenticated user by blacklisting the refresh token.",
    "request": LogoutSerializer,
    "responses": {
        200: LOGOUT_RESPONSE,
        401: LOGOUT_UNAUTHORIZED_RESPONSE,
    },
    "examples": [
        LOGOUT_REQUEST,
        LOGOUT_SUCCESS,
        LOGOUT_UNAUTHORIZED,
    ],
}