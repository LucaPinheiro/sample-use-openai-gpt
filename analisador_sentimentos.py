from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = os.getenv("OPENAI_MODEL")


def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro ao abrir o arquivo: {e}")


def salva(nome_do_arquivo, dados):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(dados)
    except IOError as e:
        print(f"Erro ao salvar o arquivo: {e}")


def analisador_sentimentos(produto):
    prompt_sistema = f"""
        Você é um analisador de sentimentos para um produto.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e depois
        atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir
        das avaliações
        
        ## Formato de sa
        
        Nome do produto: 
        Resumo das avaliações:
        Sentimento geral: [Positivo, Negativo, Neutro]
        Pontos fortes: lista de 3 pontos fortes
        Pontos fracos: lista de 3 pontos fracos
    """

    prompt_usuario = carrega(f"./texto.txt")
    print(f"Iniciou a análise do produto: {produto}")

    lista_mensagens = [
        {"role": "system", "content": prompt_sistema},
        {"role": "user", "content": prompt_usuario}
    ]

    resposta = cliente.chat.completions.create(
        messages=lista_mensagens,
        model=modelo,
    )
    
    texto_resposta = resposta.choices[0].message.content
    salva(f"./analise_{produto}.txt", texto_resposta)
    

analisador_sentimentos("Maquiagem mineral")