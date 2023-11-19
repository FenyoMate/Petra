import os
import openai

from key import Key

openai.api_key = Key


def msgContext(messages):
    context = ""
    for message in messages:
        context += "[" + message.timestamp.strftime("%Y-%m-%d %H:%M") + "] " + " User:" + message.message + "\n"
        context += "[" + message.timestamp.strftime("%Y-%m-%d %H:%M") + "] " + " Petra:" + message.answer + "\n"
        print(context)
    return context


def process(msg, context):
    print(context)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": msg}
        ],
        max_tokens=4000,
        temperature=0.6
    )
    # print("Felhasznált tokenek:" + response.usage.total_tokens)
    print(response)
    return response.choices[0].message.content
