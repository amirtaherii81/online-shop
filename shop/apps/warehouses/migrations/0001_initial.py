# Generated by Django 5.0.6 on 2024-09-08 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0012_alter_customer_image_name'),
        ('products', '0018_alter_brand_image_name_alter_product_image_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_type_title', models.CharField(max_length=50, verbose_name='نوع انبار')),
            ],
            options={
                'verbose_name': 'نوع انبار',
                'verbose_name_plural': 'انواع روش انبار',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='تعداد')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='قیمت واحد')),
                ('register_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_product', to='products.product', verbose_name='کالا')),
                ('user_registered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouseuser_registered', to='accounts.customer', verbose_name='مشتری')),
                ('warehouse_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouses', to='warehouses.warehousetype', verbose_name='انبار')),
            ],
            options={
                'verbose_name': 'انبار',
                'verbose_name_plural': 'انبارها',
            },
        ),
    ]
