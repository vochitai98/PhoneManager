# Generated by Django 4.1.7 on 2023-03-18 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_cart1_remove_cartitem_cart_remove_cartitem_product_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart1',
            new_name='Cart',
        ),
    ]
