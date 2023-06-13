# Generated by Django 4.1.7 on 2023-03-17 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LichSu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngaydat', models.TimeField()),
                ('dahang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.dathang')),
            ],
        ),
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DienThoai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=200, null=True)),
                ('gia', models.FloatField()),
                ('CPU', models.CharField(max_length=200)),
                ('manhinh', models.FloatField()),
                ('bonhotrong', models.FloatField()),
                ('camera', models.FloatField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('mota', models.CharField(blank=True, max_length=200, null=True)),
                ('noibat', models.BooleanField(default=False, null=True)),
                ('hang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.hang')),
            ],
        ),
        migrations.AddField(
            model_name='dathang',
            name='dienthoai',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.dienthoai'),
        ),
        migrations.AddField(
            model_name='dathang',
            name='khachhang',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.khachhang'),
        ),
    ]