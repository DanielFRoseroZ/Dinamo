# Generated by Django 3.1.3 on 2023-07-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo_app_gerente', '0010_autotaller_ordentrabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordentrabajo',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en proceso', 'En proceso'), ('finalizado', 'Finalizado')], default='pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='autotaller',
            name='placa',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
