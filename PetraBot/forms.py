from django import forms

from PetraBot.models import Chat


class newChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ('message', 'title', 'user')
