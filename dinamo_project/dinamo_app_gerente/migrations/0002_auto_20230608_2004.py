# Generated by Django 3.1.3 on 2023-06-09 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinamo_app_gerente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Estado',
            },
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='id_rol',
            new_name='rol',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=200, verbose_name='Correo Eléctronico'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=200, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinamo_app_gerente.estado'),
        ),
    ]
