from django.db.models.fields import NullBooleanField
from django.shortcuts import render
from .models import *
from django.templatetags.static import static
from django.contrib.auth import authenticate, login
import numpy
import imagesize
from django.contrib.sessions.models import Session
import datetime
from django.utils import timezone
from django.contrib import auth
from django.http import JsonResponse
from .forms import ShippingAddressForm, orderItemForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def aspect_ratio(prod: Product):
    img_path = static(f'images/{prod.get_default_image}')[1:]
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
    if not request.user.is_authenticated:
        if not request.session or not request.session.session_key:
            request.session.save()
            user = User.objects.all().filter(username='raunit_x')
            customer = Customer.objects.create(
                user=user[0],
                name=f'anon{request.session.session_key}',
                email='anon@genart.com',
            )
            customer.save()
            clean_expired_customers()
    context = {'products': products, 'page_title': "Shop: The Gallery of Computation"}
    return render(request, 'shop/shop.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = Customer.objects.all().filter(user=request.user)[0]
    else:
        customer = Customer.objects.all().filter(name='anon' + str(request.session.session_key))[0]

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    context = {'items': items, 'order': order, 'page_title': "Cart: The Gallery of Computation"}
    return render(request, 'shop/cart.html', context)


# id: Product id
def delete_item_from_cart(request, id):
    if request.user.is_authenticated:
        customer = Customer.objects.all().filter(user=request.user)[0]
    else:
        customer = Customer.objects.all().filter(name='anon' + str(request.session.session_key))[0]

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item_to_be_deleted = order.orderitem_set.get(product=id)
    order_item_to_be_deleted.delete()
    return cart(request)


def checkout(request):
    if request.user.is_authenticated:
        customer = Customer.objects.all().filter(user=request.user)[0]
    else:
        customer = Customer.objects.all().filter(name='anon' + str(request.session.session_key))[0]

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()

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
    if request.user.is_authenticated:
        customer = Customer.objects.all().filter(user=request.user)[0]
    else:
        customer = Customer.objects.all().filter(name='anon' + str(request.session.session_key))[0]

    selected_product = Product.objects.filter(id=id)[0]
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    item = order.orderitem_set.filter(product=id)

    if item:
        in_cart = True
    else:
        in_cart = False

    form = orderItemForm()
    images = list(selected_product.productimage_set.all())
    sorted_images = [img for img in images if img.default_image]
    for img in images:
        if not img.default_image:
            sorted_images.append(img)
    images = sorted_images
    print(form)
    context = {'product': selected_product, 'in_cart': in_cart, 'form': form, 'images': images}
    if request.method == 'POST':
        form = orderItemForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.product = selected_product
            instance.order = order
            instance.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'shop/product.html', context)


def portfolio(request):
    context = {'page_title': 'AI ART: The Gallery of Computation'}
    return render(request, 'shop/ai_art.html', context)


def updateItem(request):
    return JsonResponse('Item was added', safe=False)


def payment(request):
    return render(request, 'shop/payment.html')

def clean_expired_customers():
    customers = Customer.objects.all()
    for customer in customers:
        if customer.expiry_date and customer.expiry_date < timezone.now() :
            customer.delete()
    print("completed deleting customers at"+ str(timezone.now()))

