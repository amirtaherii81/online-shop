# Generated by Django 5.0.6 on 2024-09-12 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_order_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 12, 22, 54, 5, 291444), verbose_name='تاریخ درج سفارش'),
        ),
    ]