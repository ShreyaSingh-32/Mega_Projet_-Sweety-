from setuptools import Command
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="8b2ef82fa8bf46a3b3f9f93dcb7ce580"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)  # faster response
        audio = recognizer.listen(mic)
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("Recognized:", command)  # Debugging output
        return command

def process_command(command):
    if "open youtube" in command or "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command or "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "open flipkart" in command or "flipkart" in command:
        speak("Opening Flipkart")
        webbrowser.open("https://www.flipkart.com/")
    elif "open whatsapp" in command or "whatsapp" in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com/")
    elif any(word in command for word in  ["sweety" , "sweetie"  "sweet" ,"sweet tea","sweeti" ]):
        # Trigger word response with random choice
        speak(random.choice(["wahh", "yaa"]))
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command. lower(): 
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")   

        if r.status_code == 200:
            #  Parse the JSON response
            data = r.json()
            # print(type(data))
            # print(data.keys())

            # Extract the articles
            articles = data.get('articles',[])
        # if not articles:
        #     speak("Sorry, no news found.")
            # Print the headlines
    # else:
        for article in articles:
            
            # print("Headline:", article['title'])
            speak(article['title'])


    else:
        speak(f"I heard {Command}")
 
  
#     else:
# speak(f"I heard {Command}")

if __name__ == "__main__":
    speak("Initializing Sweety ! yaa tell me how can i help you? how can i help you? tell me")
    while True:
        try:
            print("Listening again...")
            command = listen_command()
            process_command(command)
        except Exception as e:
            print("Error:", str(e))