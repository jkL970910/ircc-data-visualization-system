# Generated by Django 4.1.2 on 2022-11-27 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0005_rename_user_id_userprofile_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="user_gender",
            field=models.CharField(default="male", max_length=250),
        ),
    ]