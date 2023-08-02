import speech_recognition as sr
import pyttsx3
from datetime import date
from time import sleep
import os
import openai


openai.api_key = "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"

class Chat:

  current_messages = []
  current_system_message = {"role": "system", "content": "You're a kind and helpful assistant"}

  def __init__(self):
    self.current_messages.append(self.current_system_message)


  # replys to chat GTP with new message, returns response, updates current_messages to show all message history
  def update_chat(self, new_message):
    global current_messages

    # creating message dict
    message_as_dict = {"role": "user", "content": new_message}

    # adding new message as dict to list of messages
    current_messages.append(message_as_dict)

    # creating chat model with updated list of messages
    completion = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = current_messages
    )

    # getting model reply
    reply = completion.choices[0].message

    # updating list of messages with model's reply
    current_messages.append(reply)

    # returning model's reply
    return reply["content"]


  # clears chat
  def clear_chat(self):
    self.current_messages = []
    self.current_messages.append(self.current_system_message)


  # changes current system message which will be updated when chat is cleared
  def change_system_message(self, new_message):
    self.current_system_message = new_message



r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()


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
        #Create a new variable to recognize current speech
        request = r.recognize_google(audio)
        #Send the request var to OpenAI
        my_prompt = Chat()
        response = my_prompt.update_chat(request)

        engine.say(response)
        engine.runAndWait()
        

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
