# Generated by Django 4.1.7 on 2023-03-18 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_cart_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
    ]