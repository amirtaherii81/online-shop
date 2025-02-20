# Generated by Django 5.0.6 on 2024-09-10 16:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0019_alter_brand_image_name_alter_product_image_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='متن نظر')),
                ('register_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ درج')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت نظر')),
                ('approving_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user2', to=settings.AUTH_USER_MODEL, verbose_name='کاربر تایید کننده نظر')),
                ('comment_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_child', to='comment_scoring_favorites.comment', verbose_name='والد نظر')),
                ('commenting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user1', to=settings.AUTH_USER_MODEL, verbose_name='کاربر نظر دهنده')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_product', to='products.product', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]
