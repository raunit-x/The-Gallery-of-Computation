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
from .forms import orderItemForm
from django.http import HttpResponseRedirect


# Create your views here.

def aspect_ratio(prod):
    img_path = static(f'images/{prod.image}')[1:]
    w, h = imagesize.get(img_path)
    return h / w


def get_size(prod):
    img_path = static(f'images/{prod.image}')[1:]
    w, h = imagesize.get(img_path)
    return w, h


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
    user = request.user
    products = list(Product.objects.all())
    products.sort(key=lambda x: aspect_ratio(x))
    for p in products:
        print(f"{p.name}: {get_size(p)}")
    context = {'products': products, 'page_title': "Shop: The Gallery of Computation"}
    return render(request, 'shop/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0}

    context = {'items': items, 'order': order, 'page_title': "Cart: The Gallery of Computation"}
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
    # fetches Product id
    in_cart = False;
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        for item in items:
            if item.product.id is id:
                in_cart = True
                break;
    else:
        in_cart = False

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
