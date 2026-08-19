import os

from twilio.rest import Client


class SMSService:
    """Send authentication OTPs through the configured SMS provider."""

    @staticmethod
    def send_otp(mobile_number: str, otp: str):
        provider = os.getenv("SMS_PROVIDER", "console").lower()

        if provider == "console":
            print(
                "\n"
                + "=" * 50
                + f"\nDEVELOPMENT OTP\nMobile Number : +91{mobile_number}"
                + f"\nOTP           : {otp}\n"
                + "=" * 50
                + "\n",
                flush=True,
            )
            return otp

        if provider != "twilio":
            raise RuntimeError(f"Unsupported SMS_PROVIDER: {provider}")

        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        from_number = os.getenv("TWILIO_FROM_NUMBER")

        missing_settings = [
            name
            for name, value in {
                "TWILIO_ACCOUNT_SID": account_sid,
                "TWILIO_AUTH_TOKEN": auth_token,
                "TWILIO_FROM_NUMBER": from_number,
            }.items()
            if not value
        ]
        if missing_settings:
            raise RuntimeError(
                "Missing Twilio settings: " + ", ".join(missing_settings)
            )

        client = Client(account_sid, auth_token)
        client.messages.create(
            body=f"Your MetaNest OTP is {otp}. It expires in 5 minutes.",
            from_=from_number,
            to=f"+91{mobile_number}",
        )

        return None