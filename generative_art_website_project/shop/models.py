from django.db import models
# Create your models here.

from django.contrib.auth.models import User
<<<<<<< HEAD
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    information = models.TextField(null=True,blank=False)
    image = models.ImageField(null=True,blank=False)
=======


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    information = models.TextField(null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
<<<<<<< HEAD
        try: 
=======
        try:
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
            url = self.image.url
        except:
            url = ''
        return url

<<<<<<< HEAD
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    @property
    def get_cart_total(self):
            orderitems = self.orderitem_set.all()
            total = sum([item.get_total for item in orderitems])
            return total
=======

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88

    # def get_cart_items(self):
    #     orderitems = self.orderitem_set.all()
    #     total = sum([item.quantity for item in orderitems])
    #     return total  
    def __str__(self):
        return str(self.id)

<<<<<<< HEAD
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
=======

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
<<<<<<< HEAD
        total = self.product.price*self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address1 = models.TextField(null=True,blank=False)
    address2 = models.TextField(null=True,blank=False)
    country = models.CharField(max_length=200,null=True)
    postal = models.IntegerField(null=True,blank=False)
    city = models.TextField(null=True,blank=False)
    state = models.TextField(null=True,blank=False)
=======
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address1 = models.TextField(null=True, blank=False)
    address2 = models.TextField(null=True, blank=False)
    country = models.CharField(max_length=200, null=True)
    postal = models.IntegerField(null=True, blank=False)
    city = models.TextField(null=True, blank=False)
    state = models.TextField(null=True, blank=False)
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address1
<<<<<<< HEAD

    
=======
>>>>>>> 932d9a4a56b77d7aaeff1385fbbacdd77a3f7f88
