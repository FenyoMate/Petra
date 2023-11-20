from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Chat(models.Model):
    title = models.CharField(max_length=100)
    context = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, default=None)
    message = models.CharField(max_length=90000)
    answer = models.CharField(max_length=90000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    time = models.DateTimeField(auto_now_add=True)


