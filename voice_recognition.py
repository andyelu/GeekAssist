import speech_recognition as sr
import pyttsx3
from datetime import date
from time import sleep




r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

print("hello")

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try: 
        words = r.recognize_google(audio)
    except:
        print("Speech not recognized")
        continue


    
    print(words)


    if words == "hey geek":
        request = r.recognize_google(audio)
        #Send request to chat gpt

    if words == "today":
        print(date.today())

    if words == "exit":
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("Goodbye")
        break
