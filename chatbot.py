import openai 

chave_api = "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"

openai.api_key=chave_api

def enviar_mensagem(mensagem):
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        prompt="Olá, como posso te ajudar hoje?",
        messages = [
            {"role":"user", "content": mensagem}
        
        ],   
        max_tokens=100
    )
    
    return resposta["choices"][0]["message"]['content']


print(enviar_mensagem("Quantos pés tem um onitorrinco?"))
