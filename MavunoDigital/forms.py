from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from MavunoDigital.models import Product, Message


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    national_id = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    national_id_back = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']


class ConsumerForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'product_category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Product Category'}),
            'product_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Description'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'quantity': forms.TextInput(attrs={' class ': 'form-control', 'placeholder': 'Quantity'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'delivery_mode': forms.TextInput(attrs={'class ': 'form-control', 'placeholder': 'Delivery Mode'}),

        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'recipient', 'body']


