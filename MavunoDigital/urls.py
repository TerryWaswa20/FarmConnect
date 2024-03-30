"""
URL configuration for FarmConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from MavunoDigital import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('farmer', views.farmer, name='farmer'),
    path('consumer', views.consumer, name='consumer'),
    path('product_form', views.product_add, name='product_add'),
    path('c_login', views.c_login, name='c_login'),
    path('f_login', views.f_login, name='f_login'),
    path('fruits', views.fruits, name='fruits'),
    path('vegetables', views.vegetables, name='veges'),
    path('cereals', views.cereals, name='cereals'),
    path('orders', views.orders, name='orders'),
    path('contact', views.contact, name='contact'),
    path('dash', views.f_dashboard, name='f_dash'),
    path('dash_b', views.dashboard, name='dash_b'),
    path('send', views.send_message, name='send_message'),
    path('inbox', views.inbox, name='inbox'),
    path('verify', views.verification, name='verify'),
    path('panel', views.verify_farmer, name='panel'),
    path('token', views.token, name='token'),
    path('pay', views.pay, name='pay'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shipping', views.shipping_address, name='shipping'),
    path('p_view', views.product_view, name='p_view'),
    path('upload', views.product_upload, name='upload'),


    path('cart_view', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('delete_product/<int:item_id>/', views.delete_product, name='delete_product'),
    path('payment', views.payment, name='payment'),

#####mpesa
    path('token', views.token, name='token'),
    path('pay', views.pay, name='pay'),
    path('stk', views.stk, name="stk")
 



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
