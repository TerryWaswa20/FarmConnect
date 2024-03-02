from django.shortcuts import render, HttpResponse, redirect
from MavunoDigital.forms import UserRegistrationForm, ConsumerForm, ProductForm, MessageForm
from MavunoDigital.models import Product, Message

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    show_product = Product.objects.all()
    return render(request, "index.html", {'show_product': show_product})


def f_login(request):
    return render(request, 'farmer_login.html')


def c_login(request):
    return render(request, 'consumer_login.html')


def farmer(request):
    submitted = False
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return render(request, "farmer_dashboard.html")
    else:
        user_form = UserRegistrationForm()
    return render(request, 'sell_on.html', {'user_form': user_form, 'submitted': submitted})


def consumer(request):
    if request.method == "POST":
        user_form = ConsumerForm(request.POST)
        if user_form.is_valid():
            user_form.save()

    else:
        user_form = ConsumerForm
    return render(request, 'consumer_register.html', {'user_form': user_form})


def product_add(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "farmer_dashboard.html")
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'product_form.html', {'form': form, 'submitted': submitted})

    form = ProductForm
    return render(request, 'product_form.html', {'form': form})


def orders(request):
    return render(request, 'consumer_orders.html')


def fruits(request):
    return render(request, 'fruits.html')


def contact(request):
    return render(request, 'contact.html')


def vegetables(request):
    vegetable_list = Product.objects.filter(product_category='Vegetable')
    return render(request, "vegetables.html",{'vegetable_list': vegetable_list})


def fruits(request):
    fruits_list = Product.objects.filter(product_category='Fruits')
    return render(request, "fruits.html",{'fruits_list': fruits_list})


def cereals(request):
    grain_list = Product.objects.filter(product_category='Grains')
    return render(request, "cereals.html",{'grain_list': grain_list})


def f_dashboard(request):
    return render(request, 'farmer_dashboard.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inbox.html')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form':form})


def inbox(request):
    received_message = Message.objects.filter(recipient=request.user.first_name)
    sent_messages = Message.objects.filter(sender=request.user.first_name)
    return render(request, 'inbox.html', {'received_message':received_message, 'sent_messages':sent_messages})




