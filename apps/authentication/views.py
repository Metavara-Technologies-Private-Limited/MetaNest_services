# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from apps.authentication.serializers.otp_serializer import SendOTPSerializer
from apps.authentication.services.auth_service import AuthService
from apps.authentication.serializers.auth_serializer import VerifyOTPSerializer


class SendOTPAPIView(APIView):
    permission_classes = [AllowAny]
    """
    API to generate and send OTP.
    """

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