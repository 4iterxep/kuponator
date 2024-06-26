# Generated by Django 5.0.6 on 2024-06-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kuponi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Магазин')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('code', models.CharField(max_length=250, verbose_name='Бонусный код/слово')),
                ('qr_code', models.ImageField(upload_to='', verbose_name='QR - код')),
                ('date_exists', models.DateField(verbose_name='До какой даты действует')),
            ],
        ),
    ]
