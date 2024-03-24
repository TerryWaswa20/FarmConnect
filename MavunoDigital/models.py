from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class Message(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Product(models.Model):

    CATEGORIES = [
        ('Vegetable', 'Vegetable'),
        ('Fruits', 'Fruits'),
        ('Grains', 'Grains')
    ]
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=20, choices=CATEGORIES)
    product_description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    product_image = models.ImageField(null='True', blank='True', upload_to='images/')
    delivery_mode = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + ' ' + self.product_category + ' ' + self.product_description



class Farmer(models.Model):
    PENDING = 'Pending'
    VERIFIED = 'Verified'
    REJECTED = 'Rejected'
    STATUS_CHOICE = [
        (PENDING, 'Pending'),
        (VERIFIED, 'Verified'),
        (REJECTED, 'Rejected')
    ]
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    location = models.CharField(max_length=50)
    id_front = models.ImageField(null='True', blank='True', upload_to='verifications/')
    id_back = models.ImageField(null='True', blank='True', upload_to='verifications/')
    status = models.CharField(max_length=50, choices=STATUS_CHOICE, default='Pending', editable=False)

    def __str__(self):
        return self.first_name + ' ' + self.location + ' ' + self.status


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE,null='True', blank='True')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null='True', blank='True')
    quantity = models.PositiveIntegerField(default=1,null='True', blank='True')
    price = models.DecimalField(max_digits=10, decimal_places=2,null='True', blank='True')
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

