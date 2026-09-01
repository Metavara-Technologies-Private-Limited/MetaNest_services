from django.db import models


class SecurityStaff(models.Model):

    ROLE_CHOICES = [
        ("Head Security", "Head Security"),
        ("Watchman", "Watchman"),
        ("Night Guard", "Night Guard"),
    ]

    SHIFT_CHOICES = [
        ("Morning", "Morning"),
        ("Evening", "Evening"),
        ("Night", "Night"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("On Leave", "On Leave"),
        ("Inactive", "Inactive"),
    ]

    name = models.CharField(max_length=100)

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES
    )

    shift = models.CharField(
        max_length=20,
        choices=SHIFT_CHOICES
    )

    phone = models.CharField(max_length=15)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    joining_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name