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
