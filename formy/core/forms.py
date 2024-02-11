from django import forms
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser

class SignupForm(CustomUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2',)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400 mb-4',
        'placeholder': 'You username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400 mb-4',
        'placeholder': 'You email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400 mb-4',
        'placeholder': 'You password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400 mb-4',
        'placeholder': 'Reenter password'
    }))


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password',)
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400 mb-4',
        'placeholder': 'You username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full border border-solid border-2 border-gray-200 outline-green-400 mb-4',
        'placeholder': 'You password'
    }))
