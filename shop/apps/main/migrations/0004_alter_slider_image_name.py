# Generated by Django 5.1.2 on 2024-10-19 15:52

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_slider_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image_name',
            field=models.ImageField(upload_to=utils.FileUpload.upload_to, verbose_name='تصویر اسلایدر'),
        ),
    ]