from django.db import models


class Role(models.Model):
    ROLE_STATUS = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    can_create = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    status = models.CharField(
        max_length=10,
        choices=ROLE_STATUS,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "roles"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name