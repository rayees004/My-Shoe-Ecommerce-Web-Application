from django.shortcuts import redirect, render

from cart.models import Cart, CartItem
from shop.models import Product

# Create your views here.
def cart_details(request):
    cart = Cart.objects.get(cart_id=c_id(request))
    cart_items = CartItem.objects.filter(CART=cart)
    return render(request,'cart.html',{'cart_items': cart_items})

def c_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=c_id(request))
    except :
        cart = Cart.objects.create(cart_id = c_id(request))
        cart.save()

    try :
        cart_item = CartItem.objects.get(PRODUCT=product, CART=cart)
        cart_item.quantity += 1
        cart_item.save()
    except :
        cart_item = CartItem.objects.create(PRODUCT=product, CART=cart, quantity=1)
        cart_item.save()
    return redirect('cart_details')


def min_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get(cart_id=c_id(request))
    cart_item = CartItem.objects.get(PRODUCT=product, CART=cart)
    if cart_item.quantity >1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_details')