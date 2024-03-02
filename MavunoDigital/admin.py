from django.contrib import admin
from MavunoDigital.models import Consumer, UserProfile, Product, Message

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Consumer)
admin.site.register(Product)
admin.site.register(Message)

