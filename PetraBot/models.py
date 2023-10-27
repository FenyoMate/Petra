from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# The message model contains a message ID, the message itself, and the sender ID.
class Message(models.Model):
    #  sender = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100000)
    message = models.CharField(max_length=100000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
