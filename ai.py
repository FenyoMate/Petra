import os
import openai

from key import Key

openai.api_key = Key


def process(msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a hungarian woman asssistant. Your job to answer the prompt questions."}, #TODO A kontextust kiegészíteni a chat tartalmával
            {"role": "user", "content": msg}
        ],
        max_tokens=2000,
        temperature=0.6
    )
   # print("Felhasznált tokenek:" + response.usage.total_tokens)
    print(response)
    return response.choices[0].message.content
