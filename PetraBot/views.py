import openai
import ratelimit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from ai import process, msgContext
from .forms import newChatForm
from .models import Chat, User, ChatMessage
import os


@login_required
def profile(request):
    chats = Chat.objects.all()
    if request.method == 'POST':
        return redirect('chat', pk=request.POST['cid'])
    return render(request, 'profile.html', {'chats': chats})


@login_required
def chat(request, pk):
    tchat = get_object_or_404(Chat, pk=pk)
    if request.method == 'POST':
        messages = ChatMessage.objects.filter(chat=tchat)
        ct = ""
        #Make messages into a string to pass to the AI
        for message in messages:
            ct += message.message + message.answer
        response = process(request.POST['chat_input'], tchat.context+ct)
        print(request.user)
        ChatMessage.objects.create(
            chat=tchat,
            message=str(request.POST.get('chat_input', False)),
            answer=str(response),
            user=request.user
        )

        tchat.save()
        return redirect( 'chat', tchat.pk)
    else:
        user = request.user
        if ChatMessage.objects.filter(chat=tchat).exists():
            messages = ChatMessage.objects.filter(chat=tchat)
            return render(request, 'chat.html', {'messages': messages})
        else:
            message = {}
            return render(request, 'chat.html', message)


@login_required
def new_chat(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = newChatForm(request.POST)
        form.user = user
        if form.is_valid():
            tchat = form.save()
            return redirect('chat', pk=tchat.pk)
    else:
        form = newChatForm()
    return render(request, 'new_chat.html', {'form': form})


def uc(request):
    return render(request, 'underconstr.html')
