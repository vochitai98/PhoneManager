# Generated by Django 4.1.7 on 2023-03-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
