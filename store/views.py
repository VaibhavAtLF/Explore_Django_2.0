from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order,Category
from decimal import Decimal
from django.db.models import Q

# Create your views here.
def product_list(request):
    query = request.GET.get('q','')
    category_filter = request.GET.get('category','')
    min_price = request.GET.get('min_price','')
    max_price = request.GET.get('max_price','')
    
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query),
        Category__name__icontains = category_filter,
        price__gte = min_price,
        price__lte = max_price
    )
    return render(request,'store/product_list.html',{
        'products':products,
        'query':query,
        'category_filer':category_filter,
        'min_price':min_price,
        'max_price':max_price
    })

#Implement Shopping Cart
def add_to_cart(request):
    product = get_object_or_404(Product)
    cart = request.session.get('cart', [])
    cart.append(product.id)
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart',[])
    products = Product.objects.filter(id__in=cart)
    return render(request,'store/view_cart.html',{'products':products})

#implement checkout process
def checkout(request):
    cart = request.session.get('cart',[])
    products = Product.objects.filter(id__in=cart)
    return render(request,'store/checkout.html',{'products':products})

@login_required
def user_dashboard(request):
    orders = Order.objects.filter(cutomer=request.user)
    return render(request,'store/user_deshboard.html',{'orders':orders})
