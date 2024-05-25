from openai import OpenAI
from dotenv import load_dotenv
import os
from token_count import calculate_costs  # Certifique-se de importar a função corretamente

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
        response_text = response.choices[0].message.content
        print(response.choices[0].message.content)
        print(response_text)
        # Passe os textos de entrada e saída para calcular os custos corretamente
        calculate_costs(model, system_prompt + user_prompt, response_text)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Exemplo de prompts
prompt = """
Você receberá uma tarefa do dia a dia. Quero que você atue como um assistente pessoal.
Sua tarefa é registrar eventos e me lembrar deles com base nas informações fornecidas.
Para cada evento, por favor, extraia e armazene os seguintes pontos chave:

- Nome do evento: Crie um nome descritivo e conciso para o evento com base nas palavras-chave fornecidas.
- Data: A data do evento.
- Local: O local do evento, se estiver especificado.
- Hora: O horário do evento.
- Descrição: Uma breve descrição do evento, com até 60 palavras.

Exemplo de entrada de evento:
"Lembre-me de um evento importante que ocorrerá na próxima semana. Vou no médico doutor Luis Carlos, na quarta-feira, às 14h. Vou fazer um check-up geral. Depois vou ver um filme para descansar."

Exemplo de saída esperada:
- Nome do evento: Check-up com Dr. Luis Carlos 
- Data: Próxima quarta-feira
- Local: Clínica do Dr. Luis Carlos
- Hora: 14h
- Descrição: Consulta médica com o Dr. Luis Carlos para um check-up geral

Certifique-se de capturar todas as informações relevantes e formatá-las de maneira clara e organizada.
"""
user_prompt = "salva que dia 15 do 3 vou ter consulta com o Dr. Carlos na clínica da rua 25 as 5 da tarde"

# Chama a função load_openai com os prompts definidos
load_openai(prompt, user_prompt)
