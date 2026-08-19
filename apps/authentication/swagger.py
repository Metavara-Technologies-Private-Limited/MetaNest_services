from drf_yasg import openapi


send_otp_success_response = openapi.Response(
    description="OTP sent successfully.",
    examples={
        "application/json": {
            "success": True,
            "message": "OTP sent successfully."
        }
    }
)