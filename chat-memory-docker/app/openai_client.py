from openai import OpenAI

client = OpenAI()  # this auto-loads your OPENAI_API_KEY from env

def get_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-4", "gpt-3.5-turbo"
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
