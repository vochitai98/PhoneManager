# Generated by Django 4.1.7 on 2023-03-18 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_listcart_delete_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListCart',
            new_name='Cart',
        ),
    ]