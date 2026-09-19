from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_add_security_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("SUPER_ADMIN", "Super Admin"),
                    ("TREASURER", "Treasurer"),
                    ("SECURITY", "Security"),
                    ("RESIDENT", "Resident"),
                ],
                default="RESIDENT",
                max_length=20,
            ),
        ),
    ]
