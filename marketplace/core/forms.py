from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        widget=forms.TextInput(attrs=({"placeholder": "Your username"}))
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs=({"placeholder": "Your email"}))
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=({"placeholder": "Your password"}))
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=({"placeholder": "Your password"}))
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs=({"placeholder": "Your username"}))
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Your password"})
    )
