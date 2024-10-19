# Generated by Django 5.0.6 on 2024-08-28 17:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_discount_alter_order_register_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_title', models.CharField(max_length=50, verbose_name='نوع پرداخت')),
            ],
            options={
                'verbose_name': 'نوع پرداخت',
                'verbose_name_plural': 'انواع روش پرداخت',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='order',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 28, 17, 7, 31, 823099), verbose_name='تاریخ درج سفارش'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_type', to='orders.paymenttype', verbose_name='نوع پرداخت'),
        ),
    ]