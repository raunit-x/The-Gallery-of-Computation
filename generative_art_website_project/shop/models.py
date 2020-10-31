from django.db import models
# Create your models here.

from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    expiry_date = models.DateTimeField(timezone.now() + datetime.timedelta(days=1),null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    information = models.TextField(null=True, blank=False)
    sold = models.BooleanField(default=False)

    # time_posted = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.name

    @property
    def get_default_image(self):
        images = list(self.productimage_set.filter(default_image=True))
        return images[0].image

    @property
    def get_default_image_url(self):
        try:
            images = list(self.productimage_set.filter(default_image=True))
            return images[0].image.url
        except Exception as e:
            print(f"Could not find the image url: {e}")
            return ''


class AIProduct(models.Model):
    name = models.CharField(max_length=200, null=True)
    information = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to='static/images')

    @property
    def get_image_url(self):
        try:
            return self.image.url
        except Exception as e:
            print(f"Some exception occurred: {e}")

        return ''


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.get_price for item in order_items])
        return total

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    signature_choices = (('Front', 'Front'), ('Back', 'Back'), ('None', 'None'))
    print_choices = (('Canvas', 'Canvas'), ('Matte Paper', 'Matte Paper'))
    printstyle = models.CharField(max_length=25, choices=print_choices, default='Canvas')
    signature = models.CharField(max_length=25, choices=signature_choices, default='Front')
    other = models.TextField(max_length=200, blank=True, null=True)

    @property
    def get_price(self):
        return self.product.price


class ShippingAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address1 = models.TextField(null=True, blank=False)
    address2 = models.TextField(null=True, blank=False)
    country = models.CharField(max_length=200, null=True)
    postal = models.IntegerField(null=True, blank=False)
    city = models.TextField(null=True, blank=False)
    state = models.TextField(null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address1


class ProductImage(models.Model):
    artwork_associated = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)
    default_image = models.BooleanField(default=False)

    @property
    def get_image_url(self):
        try:
            url = self.image.url
        except Exception as e:
            print(f"URL not found: {e}")
            url = ''
        return url


class AIProductImage(models.Model):
    artwork_associated = models.ForeignKey(AIProduct, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=False)

    @property
    def get_image_url(self):
        try:
            url = self.image.url
        except Exception as e:
            print(f"URL not found: {e}")
            url = ''
        return url
