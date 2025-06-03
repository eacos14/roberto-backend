import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("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"))

def responder(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].message.content.strip()
