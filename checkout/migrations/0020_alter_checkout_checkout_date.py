# Generated by Django 4.1.7 on 2023-04-02 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0019_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 2, 15, 16, 2, 855295, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
