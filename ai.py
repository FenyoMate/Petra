import os
import openai

openai.api_key = "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"


def process(msg):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a hungarian woman asssistant. Your job to answer the prompt questions."},
            {"role": "user", "content": msg}
        ],
        max_tokens=30,
        temperature=0.7
    )
    print(response.choices[0].message)
    return response.choices[0].message.content
