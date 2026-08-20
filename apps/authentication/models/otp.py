from django.db import models
from django.utils import timezone
from datetime import timedelta

from .user import User


class OTP(models.Model):
    PURPOSE_CHOICES = (
        ("LOGIN", "Login"),
        ("REGISTER", "Register"),
        ("FORGOT_PASSWORD", "Forgot Password"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="otps"
    )

    otp = models.CharField(max_length=6, db_index=True)

    purpose = models.CharField(
        max_length=20,
        choices=PURPOSE_CHOICES
    )

    is_verified = models.BooleanField(default=False)

    expires_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_otps"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=5)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.mobile_number} - {self.otp}"