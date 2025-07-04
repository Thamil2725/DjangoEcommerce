from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CartItem
from panther_store.models import Product
from django.shortcuts import render, redirect

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    CartItem.objects.filter(user=request.user, product=product).delete()
     # messages.warning(request, "Item removed from cart.")
    return redirect('cart_view')


@login_required
def update_cart_quantity(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
             # messages.success(request, "Quantity updated.")
        else:
            cart_item.delete()
            # messages.warning(request, "Item removed due to 0 quantity.")
    return redirect('cart_view')


@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)

    cart_products = []
    grand_total = 0

    for item in cart_items:
        subtotal = item.product.price * item.quantity
        grand_total += subtotal
        cart_products.append({
            'id': item.product.id,
            'name': item.product.name,
            'img': item.product.img,
            'cart_price': item.product.price,
            'cart_quantity': item.quantity,
            'cart_total': subtotal,
        })

    return render(request, 'cart.html', {
        'cart_products': cart_products,
        'grand_total': grand_total
    })
