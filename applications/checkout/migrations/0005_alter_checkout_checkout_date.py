# Generated by Django 4.1.7 on 2023-03-31 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 30, 16, 29, 9, 173075, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
