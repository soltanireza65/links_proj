# Generated by Django 3.1 on 2020-08-16 16:05

from django.db import migrations, models
import links.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_delete_click'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=links.models.path_and_rename),
        ),
    ]
