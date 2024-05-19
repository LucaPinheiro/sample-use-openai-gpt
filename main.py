from openai_connection import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    messages=[
        {"role": "system",
        "content": "Listar apenas os nomes dos produtos, sem considerar a descrição"
        },
        {
            "role": "user",
            "content": "Liste três produtos sustentáveis"
        }
    ],
    model='gpt-4-turbo',
    temperature=0,
    max_tokens=200,
    n = 3
)

for count in range(3):
    print(response.choices[count].message.content)