from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template.defaultfilters import floatformat
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def home(request):
    dienthoais = DienThoai.objects.all()
    hangs = Hang.objects.all()
    context ={'dienthoais':dienthoais,'hangs':hangs}
    return render(request,'app/home.html',context)

def checkout(request):
    context = {}
    return render(request,'app/checkout.html',context)

# def login(request):
#     try:
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request,user)
#             return render(request,'app/home.html')
#         else:
            
#             return HttpResponse ("Username or Password is incorrect!!!")
#             # return render(request,'app/login.html')
#     except:
#         context = {}
#         return render(request,'app/login.html',context)   
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        # context = {'username':username}
        if user is not None:
            # return render(request,'app/home.html',context)
            return redirect(reverse('home'))
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    
    return render (request,'app/login.html')
       

def register(request):
    try:
        username = request.POST['username']
        password = request.POST['password1']
        cf_password = request.POST['password2']
        # email = ""
        if password == cf_password:
            user = User.objects.create_user(username, password)
            user.save()
            return render(request,'app/login.html') 
        else:
            return render(request,'app/register.html') 
             
    except:
        context = {}
        return render(request,'app/register.html',context) 
    
def get_DTByHang(request):
    hangs= Hang.objects.all()
    id_hang = request.GET['tenhang']
    dienthoais = DienThoai.objects.filter(hang = id_hang)
    context = {'dienthoais':dienthoais,'hangs':hangs}
    return render(request,'app/home.html',context)
    # return redirect('/',con)
    
def getDTbysearch(request):
    hangs= Hang.objects.all()
    nameDT = request.GET['search']
    dienthoais = DienThoai.objects.filter(ten__contains = nameDT)
    context = {'dienthoais':dienthoais,'hangs':hangs}
    return render(request,'app/search.html',context)

def get_DTbyGia(request):
    hangs= Hang.objects.all()
    giaDT = float(request.GET['giaDT'])
    if giaDT < 5000000.0:
        dienthoais = DienThoai.objects.exclude(gia__gt = 5000000)
    elif giaDT > 5000000 and giaDT < 15000000 : 
        dienthoais = DienThoai.objects.filter(gia__gt = 5000000).exclude(gia__gt = 15000000)
    elif giaDT > 15000000:
        dienthoais = DienThoai.objects.filter(gia__gt = 15000000)
    context = {'dienthoais':dienthoais,'hangs':hangs}
    return render(request,'app/getdtbygia.html',context)

def detail(request):
    _id = int(request.GET['id'])
    hangs= Hang.objects.all()
    dt = DienThoai.objects.get(id = _id)
    context={'hangs':hangs,'dt':dt}
    return render(request,'app/detail.html',context)



def cart(request):
    # 
    context = {}
    return render(request,'app/cart.html',context)



def add_cart(request, dt_id):
    product =DienThoai.objects.get(id=dt_id)
    cart_item = Cart.objects.filter(products=product).first()
    total=0
    cart_ss = request.session.get('cart', {})
    if cart_item:       
        cart_item.soluong += 1
        cart_item.save()

      
    else:         
        new_cart_item = Cart(ten=product.ten ,products=product, soluong=1)
        new_cart_item.save()
        cart_ss[str(product.id)] = {'id': product.id, 'ten': product.ten, 'gia': product.gia, 'soluong': 1}
      
    request.session['cart_ss'] = cart_ss
    cart_items1 = Cart.objects.all()
    for item in cart_items1:
        total +=  item.products.gia * item.soluong
    context={'cart_items':cart_items1 ,'total':floatformat(total) }
    return redirect('/cart')
    # return render(request,'app/cart.html',context)
    # return redirect('cart')
def add_cart_home(request, dt_id):
    product =DienThoai.objects.get(id=dt_id)
    cart_item = Cart.objects.filter(products=product).first()
    total=0
    cart_ss = request.session.get('cart', {})
    if cart_item:       
        cart_item.soluong += 1
        cart_item.save()      
    else:         
        new_cart_item = Cart(ten=product.ten ,products=product, soluong=1)
        new_cart_item.save()
        cart_ss[str(product.id)] = {'id': product.id, 'ten': product.ten, 'gia': product.gia, 'soluong': 1}   
    request.session['cart_ss'] = cart_ss
    cart_items1 = Cart.objects.all()
    for item in cart_items1:
        total +=  item.products.gia * item.soluong
    context={'cart_items':cart_items1 ,'total':floatformat(total) }
    return redirect('/')


def remove_product(request,dt_id):
 
    product =DienThoai.objects.get(id=dt_id)
    cart_item = Cart.objects.filter(products=product).first()
    
    cart_item.delete()
    # return redirect('remove')
    # return render(request,'app/cart.html')
    return redirect('/cart')


def get_cart_items(request):
 
    cart_items = Cart.objects.all()
    return cart_items
def view_cart(request):
   
    cart_items = get_cart_items(request)
    total = sum([item.products.gia * item.soluong for item in cart_items])
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'app/cart.html', context)


def increase_quantity(request, product_id):
    product =DienThoai.objects.get(id=product_id)

    cart_item = Cart.objects.filter(products=product).first()
    if cart_item:       
        cart_item.soluong += 1
        cart_item.save()
    
    return redirect(reverse('cart'))
def decrease_quantity(request, product_id):
    product =DienThoai.objects.get(id=product_id)

    cart_item = Cart.objects.filter(products=product).first()
    if cart_item:   
        if cart_item.soluong>0 :    
         cart_item.soluong -= 1
         cart_item.save()
        if cart_item.soluong==0:
           cart_item.delete()
           
    
    return redirect(reverse('cart'))
