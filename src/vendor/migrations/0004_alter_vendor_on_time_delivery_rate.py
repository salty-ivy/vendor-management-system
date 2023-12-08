# Generated by Django 5.0 on 2023-12-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0003_alter_vendor_vendor_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="on_time_delivery_rate",
            field=models.FloatField(default=0, help_text="rate of on-time deliveries."),
        ),
    ]