# Generated by Django 5.0.6 on 2024-09-10 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_register_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 10, 16, 8, 59, 112625), verbose_name='تاریخ درج سفارش'),
        ),
    ]
