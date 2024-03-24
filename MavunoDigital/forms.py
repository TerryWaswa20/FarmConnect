
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from MavunoDigital.models import Product, Message, Farmer


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')


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


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['farmer', 'first_name', 'middle_name', 'last_name', 'id_number', 'id_front', 'id_back', 'location']



