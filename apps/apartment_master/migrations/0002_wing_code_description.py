from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apartment_master", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wing",
            name="code",
            field=models.CharField(blank=True, default="", max_length=20),
        ),
        migrations.AddField(
            model_name="wing",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
