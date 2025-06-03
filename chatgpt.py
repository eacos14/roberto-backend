import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def responder(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].message["content"].strip()
