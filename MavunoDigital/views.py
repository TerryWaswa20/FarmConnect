from django.shortcuts import render
from MavunoDigital.forms import UserRegistrationForm, ConsumerForm
from MavunoDigital.models import UserProfile, Consumer

# Create your views here.
def home(request):
    return render(request, 'index.html')


def farmer(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

    else:
        user_form = UserRegistrationForm
    return render(request, 'sell_on.html', {'user_form': user_form})


def consumer(request):
    if request.method == "POST":
        user_form = ConsumerForm(request.POST)
        if user_form.is_valid():
            user_form.save()

    else:
        user_form = ConsumerForm
    return render(request, 'consumer_register.html', {'user_form': user_form})
