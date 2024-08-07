# Generated by Django 5.0.6 on 2024-06-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('puesto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pasantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('pasantia', models.IntegerField()),
            ],
        ),
    ]
