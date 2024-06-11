import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import random
import numpy as np
import pyttsx3
from config import apikey

# Initialize the text-to-speech engine
engine = pyttsx3.init()

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        reply = response.choices[0].message["content"].strip()
        say(reply)
        chatStr += f"Chandresh: {query}\n IntelliBoT: {reply}\n"
        return reply
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't get a response."

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error: {e}")
        text += "Sorry, I couldn't get a response."

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    filename = f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt"
    with open(filename, "w") as f:
        f.write(text)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return "I didn't understand you. Please try again."
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "Could not request results; check your internet connection."

if __name__ == '__main__':
    openai.api_key = apikey
    print('Hello, I am Intelli Bot, your AI Chat Bot')
    say("Intelli Bot")
    sites = [
        ["youtube", "https://www.youtube.com"], 
        ["wikipedia", "https://www.wikipedia.com"], 
        ["google", "https://www.google.com"]
    ]
    
    while True:
        print("Listening...")
        query = takeCommand().lower()
        if "open" in query:
            for site in sites:
                if site[0] in query:
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
                    break
        elif "open music" in query:
            musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
            os.system(f"open {musicPath}")
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"The time is {hour} and {minute} minutes")
        elif "using artificial intelligence" in query:
            ai(prompt=query)
        elif "quit" in query:
            say("Goodbye!")
            break
        elif "reset chat" in query:
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)