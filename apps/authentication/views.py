# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.authentication.serializers.otp_serializer import SendOTPSerializer
from apps.authentication.services.auth_service import AuthService
from apps.authentication.serializers.auth_serializer import VerifyOTPSerializer
from rest_framework.permissions import IsAuthenticated
from apps.authentication.serializers.logout_serializer import LogoutSerializer
from apps.authentication.serializers.resend_otp_serializer import ResendOTPSerializer

from drf_spectacular.utils import (
    extend_schema,
)

from apps.authentication.swagger.auth_docs import (
    SEND_OTP_DOCS,
    VERIFY_OTP_DOCS,
    RESEND_OTP_DOCS,
    PROFILE_DOCS,
    LOGOUT_DOCS,
)

class SendOTPAPIView(APIView):
    """
    API to generate and send OTP.
    """
    permission_classes = [AllowAny]

    @extend_schema(**SEND_OTP_DOCS)

    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = AuthService.send_otp(
            mobile_number=serializer.validated_data["mobile_number"],
            role=serializer.validated_data["role"],
        )

        return Response(
            {
                "success": True,
                "message": response["message"],
            },
            status=status.HTTP_200_OK,
        )

class VerifyOTPAPIView(APIView):
    """
    API to verify OTP and login user.
    """
    permission_classes = [AllowAny]
    
    @extend_schema(**VERIFY_OTP_DOCS)

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = AuthService.verify_otp(
            mobile_number=serializer.validated_data["mobile_number"],
            otp=serializer.validated_data["otp"],
            role=serializer.validated_data["role"],
        )

        return Response(
            {
                "success": True,
                "message": response["message"],
                "data": {
                    "access": response["access"],
                    "refresh": response["refresh"],
                    "user": response["user"],
                },
            },
            status=status.HTTP_200_OK,
        )

class UserProfileAPIView(APIView):
    """
    Logged-in User Profile
    """
    permission_classes = [IsAuthenticated]
    
    @extend_schema(**PROFILE_DOCS)

    def get(self, request):

        profile = AuthService.get_profile(request.user)

        return Response(
            {
                "success": True,
                "message": "Profile fetched successfully.",
                "data": profile,
            },
            status=status.HTTP_200_OK,
        )


class LogoutAPIView(APIView):
    """
    Logout authenticated user.
    """

    permission_classes = [IsAuthenticated]

    @extend_schema(**LOGOUT_DOCS)
    
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = AuthService.logout(
            serializer.validated_data["refresh"]
        )

        return Response(
            {
                "success": True,
                "message": response["message"],
            },
            status=status.HTTP_200_OK,
        )


class ResendOTPAPIView(APIView):
    """
    API to resend login OTP.
    """

    permission_classes = [AllowAny]

    @extend_schema(**RESEND_OTP_DOCS)

    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = AuthService.resend_otp(
            mobile_number=serializer.validated_data["mobile_number"],
            role=serializer.validated_data["role"],
        )

        return Response(
            {
                "success": True,
                "message": response["message"],
            },
            status=status.HTTP_200_OK,
        )