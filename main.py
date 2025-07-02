import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key = OPENAI_KEY)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)