from openai import OpenAI
from dotenv import load_dotenv
import os

def load_openai(system_prompt, user_prompt):
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API Key for OpenAI not found in environment variables.")
    
    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL")
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            model=model,
            max_tokens=200,
        )
        
        print(response.choices[0].message.content)
    
    except Exception as e:
        print(f"An error occurred: {e}")