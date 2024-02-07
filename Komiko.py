import speech_recognition as sr
import pyttsx3
import re
import webbrowser
import matplotlib.pyplot as plt
import winsound

version = '0.1'

engine = pyttsx3.init()

responses = {
    "hello (.*)": "Hello! How are you?",
    "hello": "Hello! How are you?",
    "fine": "Oh! It's so nice to hear that.",
    "good": "Oh! It's so nice to hear that.",
    "I'm (.*)": "I'm glad to hear that. How can I help you today?",
    "who are you": "I am nobody, I am definitely not spying on you. So wanna chat?",
    "what is your name": "It's rude to ask a chatbot his/her name. ALthough I recognise as Bot",
    "what's your name": "My name's a rude secret. Give me yours.",
    "what are you": "Let's not talk about such things right now, I am an Emotion-Based Chatbot having Voice Cappabilities.",
    "what (.*) you do": "I can do what I coded to do.",
    "I need help": "if you want to search something ask SEARCH followed by your query",
    "what can you do": "I can do google search and perform all 4 basic mathematical operations",
    "do addition": "just say add number1 and number2",
    "do subtraction": "just say subtract number1 from number2",
    "do multiplication": "just say multiply number1 and number2",
    "do division": "just say divide number1 by number2",
    "(.*) how are you": "I'm well, thank you. How are you?",
    "I am a boy": "Sorry my gender contains dark humour so consider me a boy too",
    "I am a Girl": "Sorry my gender contains cuteness so consider me a girl too",
    "I am a transgender": "System Failed, Gender Out-of-Bounds :)",
    "well done": "Thanks My Master.",
    "excellent": "Thanks My Master.",
    "good work": "Thanks My Master.",
    "nice": "hehe",
    "wow":"don't be impressed yet",
}


def chatbot():
    r = sr.Recognizer()

    mic = sr.Microphone()

    while True:

        with mic as source:
            winsound.Beep(380, 350)
            audio = r.listen(source)

        text = r.recognize_google(audio)
        print(f"You said: {text}")

        if text == "goodbye":
            engine.say("Goodbye, with love from your Chearful Dearly Bot, Daddy")
            engine.runAndWait()
            print("Exiting chatbot...")
            break

        if "my name is " in text:
            global x
            x = text.replace("my name is", "", 1).strip()
            x_say = "Ok, So I will call you "+x+" from now on"
            engine.say(x_say)
            engine.runAndWait()
            print("Global Name set to {}".format(x))
            continue

        if text.startswith("search"):
            query = text.replace("search", "", 1).strip()
            print(f"Searching for: {query}")
            engine.say(f"Searching for: {query}")
            engine.runAndWait()

            google_search(query)
            continue

        if text.startswith("add"):
            queryhtml = text.strip()
            query = text.replace("add", "", 1).strip()
            print(f"Adding, {query}")
            engine.say(f"Addition of: {query}")
            engine.runAndWait()

            google(queryhtml)
            continue

        if text.startswith("subtract"):
            queryhtml = text.strip()
            query = text.replace("subtract", "", 1).strip()
            print(f"Subtracting, {query}")
            engine.say(f"Subtraction of: {query}")
            engine.runAndWait()

            google(queryhtml)
            continue

        if text.startswith("multiply"):
            queryhtml = text.strip()
            query = text.replace("multiply", "", 1).strip()
            print(f"Multiplying: {query}")
            engine.say(f"Multiplication of: {query}")
            engine.runAndWait()

            google(queryhtml)
            continue

        if text.startswith("divide"):
            queryhtml = text.strip()
            query = text.replace("divide", "", 1).strip()
            print(f"Dividing: {query}")
            engine.say(f"Quotient of: {query}")
            engine.runAndWait()

            google(queryhtml)
            continue

        for pattern, response in responses.items():
            if re.search(pattern, text):
                engine.say(response)
                engine.runAndWait()
                break

def google_search(query):
    url = f"https://google.com/search?q={query}"
    webbrowser.open_new_tab(url)

def google(queryhtml):
    url = f"https://google.com/search?q={queryhtml}"
    webbrowser.open_new_tab(url)

chatbot()