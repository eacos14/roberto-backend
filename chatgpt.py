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
