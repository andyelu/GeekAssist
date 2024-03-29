import speech_recognition as sr
from datetime import date
from time import sleep
from elevenlabs import generate, play, set_api_key
import Chat

def voice_model(text):
  """
  Takes a string as an input and outputs the string in TTS with a preset voice
  """
  audio = generate(
          text = text,
          voice = "Joe Biden"
          )
  play(audio)

  

#initializing the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

#Constantly listening to the mic input, prints "speech not recognized" when error
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

    #creating our key word
    if words == "hey geek":
    #Create a new variable to recognize current speech
        while True:
          with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
          try: 
              request = r.recognize_google(audio)
          except:
              print("Speech not recognized")
              continue
          #Key word to kill the inner while loop, taking user out of chatgpt
          if request == "exit gpt":
              print("...")
              sleep(1)
              print("...")
              sleep(1)
              print("...")
              sleep(1)
              print("Goodbye")
              break
        #Send the request var to OpenAI
          my_prompt = Chat()
          response = my_prompt.update_chat(request)
          #TTS the chatgpt response
          voice_model(response)
        
    
    if words == "today":
        print(date.today())
    #kills the program
    if request == "exit":
              print("...")
              sleep(1)
              print("...")
              sleep(1)
              print("...")
              sleep(1)
              print("Goodbye")
              break
