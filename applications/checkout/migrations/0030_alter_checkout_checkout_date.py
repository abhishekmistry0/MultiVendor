# Generated by Django 4.1.7 on 2023-06-01 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0029_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 1, 11, 12, 34, 494777, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
