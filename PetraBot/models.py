from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Chat(models.Model):
    message = models.CharField(max_length=900000)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.chat = None

    def create(self, message, title, user):
        self.message = message
        self.title = title
        self.user = user
        self.save()
        return self

    def __str__(self):
        return self.chat


