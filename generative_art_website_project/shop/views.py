from django.shortcuts import render
from .models import *


# Create your views here.

def shop(request):
    products = Product.objects.all()
    print(products)
    context = {'products': products}
    return render(request, 'shop/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'shop/checkout.html', context)
