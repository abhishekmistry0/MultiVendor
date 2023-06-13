# Generated by Django 4.1.7 on 2023-04-02 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_checkout_city_checkout_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='OrderPrice',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 2, 12, 54, 35, 821672, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
    ]
