# Generated by Django 5.1.7 on 2025-04-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0004_rename_delivery_address_delivery_delivery_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="date_delivered",
            field=models.DateTimeField(),
        ),
    ]
