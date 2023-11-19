import openai
import ratelimit
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from ai import process, msgContext
from .forms import newChatForm
from .models import Chat, User
import os


def profile(request):
    messages = Chat.objects.all()

    return render(request, 'profile.html')


@login_required
def chat(request, pk):
    chat = get_object_or_404(Chat, pk=pk)
    if request.method == 'POST':
        chat.message += (request.user + ";" +
                         request.POST['chat_input'].timestamp.strftime("%Y-%m-%d %H:%M") + ";" +
                         request.POST['chat_input'] + "\n")
        response = process(request.POST['chat_input'], request.user.chat_set.get(pk).message)
        message= {
            'sender': request.user,
            'timestamp': request.POST['chat_input'].timestamp.strftime("%Y-%m-%d %H:%M"),
            'message': request.POST['chat_input'],
            'answer': response
        }

        return render(request, 'chat.html', {'msg': message})
    else:
        user = request.user
        if user.is_authenticated:

            print(chat.message)
            msg ={
                'sender': chat.message.split(';')[0],
                'timestamp': chat.message.split(';')[1],
                'message': chat.message.split(';')[2],
                'answer': chat.message.split(';')[3]
            }
            return render(request, 'chat.html', {'msg': msg})
        else:
            return render(request, 'login.html')




@login_required
def new_chat(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = newChatForm(request.POST)
        form.message = "System: You are a woman assistant called Petra. Your job is to help your chat partner in any case."
        form.user = user
        print(form)
        tchat = form.save(commit=False)
        if form.is_valid():
            tchat.save()
            Chat.objects.create(
                message=tchat.message,
                title=tchat.title,
                user=tchat.user
            )
            return redirect('chat', pk=tchat.pk)
    else:
        form = newChatForm()
    return render(request, 'new_chat.html', {'form': form})

def uc(request):
    return render(request, 'underconstr.html')
