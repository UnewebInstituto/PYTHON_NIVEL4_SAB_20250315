# Generated by Django 5.1.7 on 2025-03-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='apellido',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='correo',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='telefono',
            field=models.CharField(max_length=250),
        ),
    ]
