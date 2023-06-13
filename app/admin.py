from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(KhachHang)
admin.site.register(Hang)
admin.site.register(DienThoai)
admin.site.register(Cart)

