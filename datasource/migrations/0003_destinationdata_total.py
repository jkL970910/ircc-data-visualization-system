# Generated by Django 4.1.2 on 2022-11-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasource", "0002_alter_categorydata_id_alter_countrydata_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="destinationdata",
            name="total",
            field=models.CharField(default="0", max_length=250),
        ),
    ]