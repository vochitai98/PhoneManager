# Generated by Django 4.1.7 on 2023-03-18 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_cart_cart1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart1',
            new_name='Cart',
        ),
    ]
