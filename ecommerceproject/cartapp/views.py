from django.shortcuts import render, redirect, get_object_or_404
from ecommerceapp.models import product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, pro_id):
    prod = product.objects.get(id=pro_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=prod, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=prod, cart=cart, quantity=1)
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        for i in cart_items:
            total += (i.product.price * i.quantity)
            counter += i.quantity

    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def cart_minus(request,pro_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    prod=get_object_or_404(product,id=pro_id)
    cart_item=CartItem.objects.get(product=prod,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def dlt(request,pro_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    prod=get_object_or_404(product,id=pro_id)
    cart_item=CartItem.objects.get(product=prod,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')