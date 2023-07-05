# Generated by Django 3.1.3 on 2023-07-05 18:59

import dinamo_app_gerente.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo_app_gerente', '0011_auto_20230705_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=10, validators=[dinamo_app_gerente.validators.validate_fecha_format])),
                ('descripcion', models.TextField()),
                ('costo_cotizacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinamo_app_gerente.autotaller')),
            ],
            options={
                'db_table': 'Cotizacion',
            },
        ),
        migrations.AddField(
            model_name='ordentrabajo',
            name='cotizacion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dinamo_app_gerente.cotizacion'),
        ),
    ]
