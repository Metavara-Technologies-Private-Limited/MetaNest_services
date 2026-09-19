from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apartment_master", "0002_wing_code_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="flat",
            name="occupancy_status",
            field=models.CharField(
                choices=[("occupied", "Occupied"), ("vacant", "Vacant")],
                default="vacant",
                max_length=20,
            ),
        ),
    ]
