# Generated by Django 5.1.7 on 2025-04-05 23:05

from django.db import migrations, models

import core.utils


class Migration(migrations.Migration):

    dependencies = [
        ("warehouses", "0012_warehouse_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="warehouse",
            name="code",
            field=models.CharField(default="000", max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name="warehouse",
            name="id",
            field=models.CharField(
                default=core.utils.generate_id,
                editable=False,
                max_length=100,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
