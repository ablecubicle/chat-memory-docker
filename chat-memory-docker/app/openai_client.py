from openai import OpenAI

client = OpenAI()  # this auto-loads your OPENAI_API_KEY from env

def get_response(prompt: str, model: str = "gpt-4o") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def list_models() -> list:
    """Return a list of available chat models from OpenAI."""
    models = client.models.list()
    # Filter for chat models (usually 'gpt' in id)
    return [m.id for m in models.data if "gpt" in m.id]
