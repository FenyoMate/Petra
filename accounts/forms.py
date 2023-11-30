from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CheckboxInput

from accounts.models import Worker, Role


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    accept = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                                label="I Accept the TNC!")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'accept')


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
    cont = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}), label="Kontextus", required=False)
    file = forms.FileField(label="Fájl feltöltése(csv,docx,txt kiterjesztések)", required=False)


class PermissionForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), label="")
    permission = forms.BooleanField(required=False, widget=CheckboxInput, label="Adminisztrátor")


class AddPositionForm(forms.Form):
    position = forms.CharField(max_length=100, label="Pozíció neve")
