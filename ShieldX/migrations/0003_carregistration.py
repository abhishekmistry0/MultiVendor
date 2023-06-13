# Generated by Django 4.1.7 on 2023-05-11 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShieldX', '0002_userrelatives_userrelativeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carHolderName', models.CharField(max_length=20)),
                ('carModel', models.CharField(max_length=20)),
                ('carMobileNumber', models.CharField(max_length=20)),
                ('carMobileEmail', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
