# from django.contrib.auth.models import User
from .models import CustomUser

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class VerifyForm(forms.Form):
    
    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder':"Email"}
            )
    )
    
class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder':"Email"}
            )
    )
    username = forms.CharField(
        help_text='Required. 25 characters or fewer. Letters, digits and _ only.',
        min_length=1,
        max_length=25,
        widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':"Username"}
            )
        )
    password1 = forms.CharField(
        help_text='Your password can’t be too similar to your other personal information. Must contain at least 8 characters. Can’t be a commonly used password. Can’t be entirely numeric.',
        label='Password',
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(
                attrs={ 'class': 'form-control', 'placeholder':"Password"}
            )
        )
    password2 = forms.CharField(
        help_text='Enter the same password as before, for verification.',
        label='Confirm Password',
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(
                attrs={ 'class': 'form-control', 'placeholder':"Confirm password"}
            )
        )

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        min_length=1,
        max_length=25,
        widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder':"Username"}
            )
        )
    password = forms.CharField(
        label='Password',
        min_length=8,
        max_length=30,
        widget=forms.PasswordInput(
                attrs={ 'class': 'form-control', 'placeholder':"Password"}
            )
        )
    
class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder':"Email"}
            )
    )
