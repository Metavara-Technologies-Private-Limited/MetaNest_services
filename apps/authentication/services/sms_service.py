class SMSService:
    """
    SMS Service.
    Replace this implementation with MSG91/Twilio in production.
    """

    @staticmethod
    def send_otp(mobile_number: str, otp: str):
        print("\n" + "=" * 50)
        print("OTP SENT")
        print(f"Mobile Number : {mobile_number}")
        print(f"OTP           : {otp}")
        print("=" * 50 + "\n")

        return True