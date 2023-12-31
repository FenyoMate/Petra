import tiktoken
from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)


class Worker(models.Model):
    title = models.ForeignKey(Role, on_delete=models.CASCADE, default=None)
    desk = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class superContext(models.Model):
    context = models.CharField(max_length=90000)
    value = models.IntegerField(default=0)



class upContext(models.Model):
    uploaded_files = models.FileField(upload_to='static/contexts/')

    def delete(self, *args, **kwargs):
        if self.uploaded_files:
            storage, path = self.uploaded_files.storage, self.uploaded_files.path
            storage.delete(path)

        super().delete(*args, **kwargs)
