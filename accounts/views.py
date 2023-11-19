from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm, LoginForm


# Create your views here.

#@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(LoginForm, data=request.POST)
        if form.is_valid():
            print("valid")
            user = form.get_user()
            auth_login(request, user)
            return render(request, 'chat.html', {'user': user})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            User.objects.create(user)
            auth_login(request, user)

            return render(request, 'profile.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def logout(request):
    user = request.user
    if user.is_authenticated:
        user = None
        request.session.flush()
    return redirect('login')