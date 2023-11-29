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
        temperature=0.4
    )
    return response.choices[0].message.content


def img_process(img):
    print(img)
    sc = get_object_or_404(superContext, id=1)
    bc = "A következő az előre megadott kontextusod: " + sc.context + "\n"
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "Elemezd alaposan az ábrát és részletesen foglald össze a látottakat." + bc},
            {
                "role": "system",
                "content": img,
            },

        ],
        max_tokens=4000,
        temperature=0.4
    )
    print(response)
    return response.choices[0]
