# Generated by Django 5.1.7 on 2025-03-30 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import core.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileUser",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=core.utils.generate_id,
                        editable=False,
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "warehouse_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
