import queue
import sounddevice as sd
import vosk
import json

model = vosk.Model("path_to_vosk_model")
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen_for_command(callback):
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("Listening for 'segunda' to start the command...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result['text']
                if 'segunda' in text.lower():
                    print(f"Trigger word detected: {text}")
                    while True:
                        print("Listening for command after trigger word...")
                        data = q.get()
                        if rec.AcceptWaveform(data):
                            result = json.loads(rec.Result())
                            command_text = result['text']
                            print(f"Command recognized: {command_text}")
                            callback(command_text)
                            break

if __name__ == "__main__":
    listen_for_command(lambda text: print(f"Comando recebido: {text}"))
