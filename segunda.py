import requests
import json

url = "http://146.235.56.158:8000/chat"

headers = {
    "Content-Type": "application/json"
}

def enviar_mensagem(mensagem):
    data = {"message": mensagem}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json().get("response", "Erro: resposta inesperada do servidor.")
    else:
        return f"Falha na solicitação: {response.status_code}, {response.text}"

def chatbot():
    print("Oá sou Segunda!")
    
    while True:
        mensagem = input("Você: ")
        
        if mensagem.lower() == 'adeus':
            print("Até um dia!.")
            break
        
        resposta = enviar_mensagem(mensagem)
        print("SEGUNDA:", resposta)

if __name__ == "__main__":
    chatbot()
