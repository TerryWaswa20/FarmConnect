from django.contrib import admin
from MavunoDigital.models import Product, Message, Farmer, ShippingAddress, CartItem


class FarmerAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'status']
    list_filter = ['status']
    actions = ['verified', 'rejected']

    def verified(self, request, queryset):
        queryset.update(status = Farmer.VERIFIED)
    verified.short_description = "Mark Selected farmer verified"

    def rejected(self, request, queryset):
        queryset.update(status= Farmer.REJECTED)
    rejected.short_description = "Mark selected farmer rejected"


# Register your models here.
admin.site.register(Product)
admin.site.register(Message)
admin.site.register(Farmer, FarmerAdmin)
admin.site.register(ShippingAddress)
admin.site.register(CartItem)

