from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MavunoDigital.urls')),
]

admin.site.site_header = "Mavuno Digital Admin Site"
admin.site.site_title = "Mavuno Digital"
admin.site.index_title = "Welcome To Mavuno Digital"
