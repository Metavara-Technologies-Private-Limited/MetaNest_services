from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


mobile_validator = RegexValidator(
    regex=r"^[6-9]\d{9}$",
    message="Enter a valid 10-digit mobile number.",
)


class UserManager(BaseUserManager):
    """
    Custom User Manager.
    """

    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError("Mobile number is required.")

        mobile_number = str(mobile_number).strip()

        user = self.model(
            mobile_number=mobile_number,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            mobile_number=mobile_number,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model using mobile number for authentication.
    """

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        RESIDENT = "RESIDENT", "Resident"

    mobile_number = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        validators=[mobile_validator],
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    email = models.EmailField(
        blank=True,
        default=""
    )

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.RESIDENT,
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "mobile_number"

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.mobile_number} ({self.role})"