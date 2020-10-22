from django.shortcuts import render
from .models import *
<<<<<<< HEAD
=======


>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
# Create your views here.

def shop(request):
    products = Product.objects.all()
    print(products)
<<<<<<< HEAD
    context = {'products':products}
    return render(request,'shop/shop.html',context)

def cart(request):

=======
    context = {'products': products}
    return render(request, 'shop/shop.html', context)


def cart(request):
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
<<<<<<< HEAD
        order = {'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'shop/cart.html',context)
=======
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)

>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
<<<<<<< HEAD
        order = {'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'shop/checkout.html',context)
=======
        order = {'get_cart_total': 0}
    context = {'items': items, 'order': order}
    return render(request, 'shop/checkout.html', context)
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
