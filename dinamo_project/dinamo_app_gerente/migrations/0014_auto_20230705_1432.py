# Generated by Django 3.1.3 on 2023-07-05 19:32

import dinamo_app_gerente.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo_app_gerente', '0013_auto_20230705_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='foto',
            field=models.FileField(upload_to='fotos_autos', validators=[dinamo_app_gerente.validators.validate_file_extension_imgs]),
        ),
    ]
