# Generated by Django 4.1.1 on 2022-09-14 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0010_alter_persona_id_persona_alter_persona_login_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='login_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='login_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
