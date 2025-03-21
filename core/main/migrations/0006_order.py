# Generated by Django 4.2.19 on 2025-03-08 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_paymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Приянто')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Количество')),
                ('check_image', models.ImageField(upload_to='media/check', verbose_name='Чек')),
                ('status', models.CharField(choices=[('in_processing', 'В обработке'), ('denied', 'Отклонено'), ('accepted', 'Принято')], default='in_processing', max_length=15, verbose_name='Статус оплаты')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка на оплату',
                'verbose_name_plural': 'Заявки на оплату',
            },
        ),
    ]
