from django.shortcuts import render
from .models import *
from django.templatetags.static import static
from PIL import Image
import numpy
import imagesize


# Create your views here.

def aspect_ratio(prod):
    img_path = static(f'images/{prod.image}')[1:]
    w, h = imagesize.get(img_path)
    return h / w


def shop(request):
    products = list(Product.objects.all())
    products.sort(key=lambda x: aspect_ratio(x))
    context = {'products': products, 'page_title': "Shop: The Gallery of Computation" }
    return render(request, 'shop/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order, 'page_title': "Cart: The Gallery of Computation" }
    return render(request, 'shop/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order, 'page_title': "Cart: The Gallery of Computation"}
    return render(request, 'shop/checkout.html', context)

def product(request, id):
    #fetches Product id 
    product = Product.objects.filter(id=id)
    print(product)
    context = {'product': product[0]}
    return render(request,'shop/product.html',context )

def portfolio(request, id):
    #fetches Product id 
    product = Product.objects.filter(id=id)
    print(product)
    context = {'product': product[0]}
    return render(request,'shop/portfolio.html',context )

