# Generated by Django 4.1.7 on 2023-03-31 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 30, 16, 30, 36, 131721, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
