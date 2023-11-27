from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CheckboxInput

from accounts.models import Worker, Role


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    accept = forms.BooleanField(widget=CheckboxInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class CategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class SetupForm(forms.ModelForm):
    title = CategoryChoiceField(queryset=Role.objects.all())

    class Meta:
        model = Worker
        fields = ('name', 'firstname', 'lastname', 'title', 'desk')


class UploadContextForm(forms.Form):
    cont = forms.CharField(max_length=50000)
    file = forms.FileField()
