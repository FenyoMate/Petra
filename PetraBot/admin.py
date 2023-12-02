from django.contrib import admin
from django.contrib.auth.models import User

from .models import Chat, ChatMessage

# Register your models here.

admin.site.register(Chat)
admin.site.register(ChatMessage)