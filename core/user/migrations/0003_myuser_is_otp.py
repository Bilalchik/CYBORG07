# Generated by Django 4.2.19 on 2025-03-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_otp',
            field=models.BooleanField(default=False),
        ),
    ]
