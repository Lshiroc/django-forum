from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400',
        'placeholder': 'You username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400',
        'placeholder': 'You email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400',
        'placeholder': 'You password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400',
        'placeholder': 'Reenter password'
    }))
