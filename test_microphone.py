
from voice.speech_to_text import listen

spoken_text = listen()

if spoken_text:
    print("Final text:", spoken_text)
