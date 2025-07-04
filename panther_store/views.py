from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from panther_store.models import Product


# Create your views here.

from cart.models import CartItem  # import your CartItem model if not already

def show_homepage(request):
    products = Product.objects.all()

    cart = CartItem.objects.filter(user=request.user) if request.user.is_authenticated else []

    return render(request, 'index.html', {
        'products': products,
        'cart': cart
    })


