import openai
import ratelimit
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator

from ai import process
from .models import Message
import os


def profile(request):
    return render(request, 'profile.html')


def chat(request):
    messages = Message.objects.all()

    if request.method == 'POST':
        message = request.POST['chat_input']

        response = process(message)

        Message.objects.create(message=message, answer=response)
        return redirect(request, 'chat.html')
    print(request.user.is_authenticated)
    return render(request, 'chat.html', {'msg': messages})


def profile(request):
    return render(request, 'profile.html')


def uc(request):
    return render(request, 'underconstr.html')