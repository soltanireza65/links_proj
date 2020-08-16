# Generated by Django 3.1 on 2020-08-13 06:00

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='users/profilePic.png', null=True, upload_to=accounts.models.path_and_rename),
        ),
    ]