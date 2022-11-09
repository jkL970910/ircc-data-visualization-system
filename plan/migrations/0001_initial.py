# Generated by Django 4.1 on 2022-11-08 06:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "plan_name",
                    models.CharField(
                        blank=True, default="monthly", max_length=250, unique=True
                    ),
                ),
                (
                    "plan_price",
                    models.CharField(blank=True, default="200", max_length=250),
                ),
            ],
            options={
                "db_table": "plan",
                "managed": True,
            },
        ),
    ]