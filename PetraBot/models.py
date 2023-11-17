from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100000)
    message = models.CharField(max_length=3000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.CharField(max_length=900000)
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.chat = None

    def __str__(self):
        return self.chat

    def __exceed__(self):
        return self.context.__sizeof__()
