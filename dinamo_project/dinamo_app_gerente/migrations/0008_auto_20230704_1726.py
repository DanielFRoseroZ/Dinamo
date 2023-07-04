# Generated by Django 3.1.3 on 2023-07-04 22:26

import dinamo_app_gerente.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo_app_gerente', '0007_auto_20230704_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credito',
            old_name='cedula_cliente',
            new_name='cliente',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=200, unique=True, validators=[dinamo_app_gerente.validators.validate_email], verbose_name='Correo Eléctronico'),
        ),
    ]
