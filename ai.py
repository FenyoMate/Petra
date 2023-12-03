import os
import openai
import tiktoken
from django.shortcuts import get_object_or_404

from PetraBot.models import ChatMessage
from accounts.models import superContext

from key import Key

openai.api_key = Key


def process(msg, context, cid):
    sc = get_object_or_404(superContext, id=1)
    ct = "A következő az előre megadott kontextusod: " + sc.context + "\n"
    ct += "A következő kérdéseket tettem fel korábban és válaszoltál rájuk. Ez a te kontextusod: \n" + context
    sc.save()
    if ChatMessage.objects.filter(chat=cid) is not None:
        co = ChatMessage.objects.filter(chat=cid)
        co.tokens = co.last()
        print(co.tokens)
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": ct},
            {"role": "user", "content": msg}
        ],
        max_tokens=4000,
        temperature=0.6
    )
    print(response)
    print(sc.value)

    return response.choices[0].message.content
