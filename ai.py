import os
import openai

from key import Key

openai.api_key = Key


def process(msg, context):
    print(context)
    ct = "A következő kérdéseket tettem fel korábban és válaszoltál rájuk. Ez a te kontextusod: " + context
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": ct},
            {"role": "user", "content": msg}
        ],
        max_tokens=4000,
        temperature=0.4
    )
    # print("Felhasznált tokenek:" + response.usage.total_tokens)
    print(response)
    return response.choices[0].message.content
