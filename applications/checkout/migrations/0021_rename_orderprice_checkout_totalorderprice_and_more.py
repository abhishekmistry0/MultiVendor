# Generated by Django 4.1.7 on 2023-04-27 07:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_reviews_product_review'),
        ('checkout', '0020_alter_checkout_checkout_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='OrderPrice',
            new_name='totalOrderPrice',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='product_qty',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='products_id',
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 27, 7, 48, 19, 587062, tzinfo=datetime.timezone.utc), verbose_name='expiration time (of ad)'),
        ),
        migrations.CreateModel(
            name='OrdersItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderedItemQuantity', models.CharField(max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='checkout.checkout')),
                ('ordersItem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
