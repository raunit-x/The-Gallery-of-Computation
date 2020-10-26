from django.shortcuts import render
from .models import *
from django.templatetags.static import static
from django.contrib.auth import authenticate, login
from PIL import Image
import numpy
import imagesize
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.contrib import auth
from django.http import JsonResponse
from .forms import ShippingAddressForm, orderItemForm
from django.http import HttpResponseRedirect


# Create your views here.

def aspect_ratio(prod):
    img_path = static(f'images/{prod.image}')[1:]
    w, h = imagesize.get(img_path)
    return h / w


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


def shop(request):
    products = list(Product.objects.all())
    products.sort(key=lambda x: aspect_ratio(x))
    context = {'products': products, 'page_title': "Shop: The Gallery of Computation"}
    return render(request, 'shop/shop.html', context)


def cart(request):
    items = []
    order = {'get_cart_total': 0}
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    context = {'items': items, 'order': order, 'page_title': "Cart: The Gallery of Computation"}
    return render(request, 'shop/cart.html', context)


# id: Product id
def delete_item_from_cart(request, id):
    order = {'get_cart_total': 0}
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item_to_be_deleted = order.orderitem_set.get(product=id)
    order_item_to_be_deleted.delete()
    return cart(request)


def checkout(request):
    items = []
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    form = ShippingAddressForm()
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.order = order
            instance.save()
            return render(request, 'shop/payment.html')
    context = {'items': items, 'order': order, 'page_title': "Checkout: The Gallery of Computation", 'form': form}
    return render(request, 'shop/checkout.html', context)


# id: Product id
def product(request, id):
    in_cart = False
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        item = order.orderitem_set.filter(product=id)
        if item:
            in_cart = True

    customer = request.user.customer
    selected_product = Product.objects.filter(id=id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    form = orderItemForm()
    context = {'product': selected_product[0], 'in_cart': in_cart, 'form': form}
    if request.method == 'POST':
        form = orderItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.product = selected_product[0]
            instance.order = order
            instance.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'shop/product.html', context)


def portfolio(request, id):
    # fetches Product id
    selected_product = Product.objects.filter(id=id)
    context = {'product': selected_product[0]}
    return render(request, 'shop/portfolio.html', context)


def updateItem(request):
    return JsonResponse('Item was added', safe=False)


def payment(request):
    return render(request, 'shop/payment.html')
