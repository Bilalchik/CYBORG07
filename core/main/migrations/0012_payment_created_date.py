# Generated by Django 4.2.19 on 2025-03-18 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_payment_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
