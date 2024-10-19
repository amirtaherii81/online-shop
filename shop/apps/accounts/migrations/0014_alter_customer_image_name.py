# Generated by Django 5.0.6 on 2024-09-12 00:26

import utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_customer_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image_name',
            field=models.ImageField(blank=True, null=True, upload_to=utils.FileUpload.upload_to, verbose_name='تصویر پروفایل'),
        ),
    ]
