# Generated by Django 4.1.7 on 2023-04-02 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_reviews_product_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='product_review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
