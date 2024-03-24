from django.contrib import admin
from MavunoDigital.models import Product, Message, Farmer


class FarmerAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'status']
    list_editable = ['status']


# Register your models here.
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(Farmer)

