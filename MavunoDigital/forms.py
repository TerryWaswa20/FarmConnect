from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(help_text='YYYY-MM-DD')
    national_id = forms.ImageField(label='ID Card Front')
    national_id_back = forms.ImageField(label='ID Card Back')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2']

        widgets = {
          'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
          'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
          'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-mm-dd'}),
          'password1': forms.PasswordInput(attrs={' class ': 'form-control', 'placeholder': 'Create Password'}),
          'password2': forms.PasswordInput(attrs={' class ': 'form-control', 'placeholder': 'Confirm Password'}),

         }


class ConsumerForm(UserCreationForm):
      email = forms.EmailField()
      first_name = forms.CharField(max_length=100)
      last_name = forms.CharField(max_length=100)

      class Meta:
          model = User
          fields = ['email', 'first_name', 'last_name', 'password', 'password1']

