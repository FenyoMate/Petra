import os
import openai

openai.api_key_path = os.getenv("OPENAI_API_KEY_PATH")


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
   # print("Felhasznált tokenek:" + response.usage.total_tokens)
    print(response)
    return response.choices[0].message.content
