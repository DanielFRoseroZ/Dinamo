# Generated by Django 3.1.3 on 2023-06-29 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo_app_gerente', '0004_auto_20230614_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='correo',
            new_name='username',
        ),
    ]
