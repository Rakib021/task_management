from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(UserCreationForm):   
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        

    username = forms.CharField(
        label='',  
        help_text='',  
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label='',  
        help_text='',  
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label='',  
        help_text='',  
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']