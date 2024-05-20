from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
import os

load_dotenv()

def calculate_costs(model, input_text, output_text):
    encoder = tiktoken.encoding_for_model(model)
    
    input_tokens = encoder.encode(input_text)
    output_tokens = encoder.encode(output_text)
    
    # Contagem de tokens
    input_token_count = len(input_tokens)
    output_token_count = len(output_tokens)
    total_token_count = input_token_count + output_token_count
    
    # Tarifas por 1k tokens
    input_cost_per_1k = 0.015  # $0.015 por 1k tokens de entrada
    output_cost_per_1k = 0.03  # $0.03 por 1k tokens de saída
    
    input_cost = (input_token_count / 1000) * input_cost_per_1k
    output_cost = (output_token_count / 1000) * output_cost_per_1k
    total_cost = input_cost + output_cost
    
    print("Tokens de entrada: ", input_token_count)
    print("Tokens de saída: ", output_token_count)
    print("Tokens totais: ", total_token_count)
    print(f"Custo para a entrada: ${input_cost:.6f}")
    print(f"Custo para a saída: ${output_cost:.6f}")
    print(f"Custo total: ${total_cost:.6f}")