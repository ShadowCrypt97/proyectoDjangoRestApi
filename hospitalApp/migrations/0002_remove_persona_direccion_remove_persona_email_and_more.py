# Generated by Django 4.1.1 on 2022-09-11 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='email',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='tipoDoc',
        ),
    ]
