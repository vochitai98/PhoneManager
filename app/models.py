from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         # if not email:
#         #     raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             # email=self.normalize_email(email),
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     # email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'username'
#     # REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin
    



from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class KhachHang(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Hang(models.Model):
    ten =  models.CharField(max_length=200,null = True,blank=False)
    def __str__(self):
        return self.ten
class DienThoai(models.Model):
    ten = models.CharField(max_length=200,null = True)
    gia = models.FloatField()
    CPU = models.CharField(max_length=200,blank=False)
    manhinh =  models.FloatField()
    bonhotrong = models.FloatField()
    camera = models.FloatField(null=True)
    hang = models.ForeignKey(Hang,on_delete=models.SET_NULL,blank=True,null=True)
    image = models.ImageField(null=True,blank=True)
    mota = models.CharField(max_length=200,null= True,blank=True)
    noibat = models.BooleanField(default=False,null=True,blank=False)

    def __str__(self):
        return self.ten
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Cart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    ten = models.CharField(max_length=200,null = True)
    # soluong = models.IntegerField()
    # gia = models.FloatField()
    # total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    # products = models.ManyToManyField(DienThoai)

    products = models.ForeignKey(DienThoai, on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    soluong = models.IntegerField(default=0)
  
    # gia = models.FloatField()
    def __iter__(self):
        yield 'ten', self.ten
        # yield 'user', self.user
        # yield 'products', self.products
        yield 'soluong', self.soluong
        # yield 'gia', self.gia
        # yield 'total', self.total