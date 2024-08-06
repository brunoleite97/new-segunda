import pywhatkit as kit

def yt_play(*args, **kwargs):
    inp_command = kwargs.get("query")
    if inp_command:
        kit.playonyt(inp_command)
        return f"Tocando '{inp_command}' no YouTube."
    else:
        return "Nenhuma música especificada."

if __name__ == "__main__":
    print(yt_play(query='Enter Sandman'))
