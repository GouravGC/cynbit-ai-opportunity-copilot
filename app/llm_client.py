import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY is missing from .env")

client = OpenAI(
    api_key = api_key,
    base_url = "https://openrouter.ai/api/v1",
    timeout = 60,
    max_retries = 1,
)

def generate_response(prompt:str)->str:
    response = client.chat.completions.create(
        model = "google/gemini-2.5-flash",
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature = 0.2,
        max_tokens = 500,
    )

    return response.choices[0].message.content