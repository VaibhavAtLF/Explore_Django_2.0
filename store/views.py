from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from .models import Product
def product_list(request):
    products = Product.objects.all()
    return render(request,'store/product_list.html',{'products':products})

#Implement Shopping Cart
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    cart = request.session.get('cart',[])
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
