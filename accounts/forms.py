from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from accounts.models import Worker


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SetupForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'firstname', 'lastname', 'title', 'desk')
