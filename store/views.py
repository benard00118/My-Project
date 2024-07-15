from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

def cart(request):
    # Logic for displaying items in the cart
    return render(request, 'store/cart.html')

def checkout(request):
    # Logic for handling checkout
    return render(request, 'store/checkout.html')
