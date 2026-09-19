from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0002_remove_securitystaff_assigned_block_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="resident",
            name="email",
            field=models.EmailField(blank=True, default="", max_length=254),
        ),
    ]
