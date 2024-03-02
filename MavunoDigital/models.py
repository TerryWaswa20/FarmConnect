from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()


class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    product_image = models.ImageField(null='True', blank='True', upload_to='images/')
    delivery_mode = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + ' ' + self.product_category + ' ' + self.product_description




