import PyPDF2
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.views.decorators.csrf import csrf_exempt
from docx import Document

from doc_handling import docx, handle
from .models import Worker, superContext, Role, upContext
from .forms import SignUpForm, LoginForm, SetupForm, UploadContextForm, PermissionForm, AddPositionForm


# Create your views here.

# @csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(LoginForm, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('setup')
    else:
        form = SignUpForm()
        form.accept = False
    return render(request, 'signup.html', {'form': form})


@login_required
def logout(request):
    user = request.user
    if user.is_authenticated:
        user = None
        request.session.flush()
    return redirect('login')


@login_required
def profileSetup(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if Worker.objects.filter(user=user).exists():
        if request.method == 'POST':
            form = SetupForm(request.POST)
            form.user = user
            if form.is_valid():
                user = form.save(commit=False)
                user.user = request.user
                worker = get_object_or_404(Worker, user=request.user)
                worker.title = user.title
                worker.desk = user.desk
                worker.name = user.name
                worker.firstname = user.firstname
                worker.lastname = user.lastname
                worker.save()
                return redirect('profile')
    if request.method == 'POST':
        form = SetupForm(request.POST)
        form.user = user
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            return redirect('profile')
    else:
        form = SetupForm()
    return render(request, 'profileSetup.html', {'form': form})


def settings(request):
    return render(request, 'settings.html')


def context(request):
    contxt = get_object_or_404(superContext, pk=1)
    if request.method == 'POST':
        form = UploadContextForm(request.POST, request.FILES or None)
        print(form)
        if form.is_valid():
            tstr = ""
            if request.FILES.get('file', False):
                print(request.FILES)
                upfile = request.FILES['file']
                print(upfile)
                if upContext.objects.exists():
                    for pk in upContext.objects.all():
                        pk.delete()
                upfiles = upContext.objects.create(uploaded_files=upfile)
                print(upfiles.uploaded_files)
                upfiles.save()
                tstr = handle(upfiles.uploaded_files.name)
            tstr += '\n' + request.POST['cont']
            contxt.context = markdown.markdown(tstr)
            contxt.save()
            return redirect('context')
    form = UploadContextForm()
    return render(request, 'context.html', {'form': form, 'context': contxt.context})
