from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("SECURITY", "Security"),
                    ("RESIDENT", "Resident"),
                ],
                default="RESIDENT",
                max_length=20,
            ),
        ),
    ]
