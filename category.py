from openai_connection import load_openai

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
user =  """
 prova de calculo dia 13 as 14h na Maua
    """
    
load_openai(prompt, user)
