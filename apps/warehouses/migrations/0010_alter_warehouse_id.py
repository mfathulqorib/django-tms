# Generated by Django 5.1.7 on 2025-04-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouses", "0009_alter_warehouse_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="warehouse",
            name="id",
            field=models.CharField(
                max_length=50, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
