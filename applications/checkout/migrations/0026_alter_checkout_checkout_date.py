# Generated by Django 4.1.7 on 2023-06-01 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0025_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 1, 10, 18, 21, 850545, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
