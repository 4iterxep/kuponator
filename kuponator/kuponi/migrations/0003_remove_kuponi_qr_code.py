# Generated by Django 5.0.6 on 2024-06-09 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kuponi', '0002_alter_kuponi_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kuponi',
            name='qr_code',
        ),
    ]