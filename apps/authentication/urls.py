from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from apps.authentication.views import (
    SendOTPAPIView,
    VerifyOTPAPIView,
    UserProfileAPIView,
    LogoutAPIView,
    ResendOTPAPIView,
)

urlpatterns = [
    path(
        "send-otp/",
        SendOTPAPIView.as_view(),
        name="send-otp",
    ),

    path(
        "verify-otp/",
        VerifyOTPAPIView.as_view(),
        name="verify-otp",
    ),

    path(
        "profile/",
        UserProfileAPIView.as_view(),
        name="profile",
    ),

    path(
        "logout/",
        LogoutAPIView.as_view(),
        name="logout",
    ),

    path(
    "token/refresh/",
    TokenRefreshView.as_view(),
    name="token_refresh",
    ),

    path(
    "resend-otp/",
    ResendOTPAPIView.as_view(),
    name="resend-otp",
    ),

    path(
    "token/verify/",
    TokenVerifyView.as_view(),
    name="token_verify",
    ),
]