from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

class UserProfileChange(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_picture',)
        labels = {
            'profile_picture': '',
        }

    profile_picture = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'absolute inset-0 opacity-0'
    }))
