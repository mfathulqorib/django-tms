# Generated by Django 5.1.7 on 2025-04-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0006_alter_delivery_date_delivered_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="estimated_time_arrival",
            field=models.DateField(verbose_name="ETA"),
        ),
    ]
