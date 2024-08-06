from operation.speakOffline import speak
from operation.chat import enviar_mensagem
from operation.listen import listen_for_command
from features.youtb import yt_play
from features.velocidade import speed_test

def process_command(command_text):
    command_text_lower = command_text.lower()

    if "tocar" in command_text_lower:
        query = command_text_lower.replace("tocar", "").strip()
        response = yt_play(query=query)
    elif "teste de velocidade" in command_text_lower:
        response = speed_test()
    else:
        response = enviar_mensagem(command_text_lower)
    
    speak(response)

def main():
    listen_for_command(process_command)

if __name__ == "__main__":
    main()
