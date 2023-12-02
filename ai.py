import os
import openai
from django.shortcuts import get_object_or_404

from accounts.models import superContext

from key import Key

openai.api_key = Key


def process(msg, context):
    sc = get_object_or_404(superContext, id=1)
    ct = "A következő az előre megadott kontextusod: " + sc.context + "\n"
    ct += "A következő kérdéseket tettem fel korábban és válaszoltál rájuk. Ez a te kontextusod: \n" + context
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": ct},
            {"role": "user", "content": msg}
        ],
        max_tokens=4000,
        temperature=0.5
    )
    print(response)
    return response.choices[0].message.content


