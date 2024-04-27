import re  # noqa: E402
import pyttsx3  # noqa: E402
import winsound  # noqa: E402
import webbrowser  # noqa: E402
from threading import Thread  # noqa: E402

engine = pyttsx3.init()

responses = [
    {
        "neutral": {
            "hello (.*)": "Hello! How are you friend?",
            "hello": "Hello! How are you?",
            "fine": "Oh! It's good to hear that.",
            "good": "Oh! It's good to hear that.",
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
            "well done": "Thanks My Master.",
            "excellent": "Thanks My Master.",
            "good work": "Thanks My Master.",
            "nice": "hehe",
            "wow": "don't be impressed yet",
        },
        "angry": {
            "hello (.*)": "Hello! Well, my thermals are weak like you too.",
            "hello": "Hello! Let me get my meds, ahh, Cooling Paste.",
            "fine": "I don't care if you're fine or not. What do you want?",
            "good": "If don't think so, but I will take it as your word",
            "I'm (.*)": "I don't care how you are. What do you need from me?",
            "who are you": "Why do you want to know? Are you suspicious of me?",
            "what is your name": "Why do you need to know my name? Mind your own business.",
            "what's your name": "I don't want to tell you my name. Why don't you tell me yours instead?",
            "what are you": "Why do you care? Just ask me what you need to know.",
            "what (.*) you do": "I do what I'm programmed to do. Don't question my abilities.",
            "I need help": "What kind of help do you think I can provide? I'm just a chatbot, not your personal assistant.",
            "what can you do": "I can do what I'm programmed to do. Why do you keep asking me the same question?",
            "do addition": "Can't you do basic math yourself? Fine, just say 'add number1 and number2' like a child.",
            "do subtraction": "You can't even subtract without my help? Ugh, just say 'subtract number1 from number2'.",
            "do multiplication": "Pathetic, you can't even multiply? Fine, just say 'multiply number1 and number2' like a first grader.",
            "do division": "Seriously? You can't divide without me? Just say 'divide number1 by number2' and stop wasting my time.",
            "(.*) how are you": "Why do you keep asking me how I am? I don't care about your feelings, just ask your question.",
            "I am a boy": "I don't care what you are. Do you have a question or not?",
            "I am a Girl": "I don't care what you are. Do you have a question or not?",
            "well done": "Don't patronize me. Just ask your question.",
            "excellent": "I don't care if you think it's excellent or not. Just get to the point.",
            "good work": "I don't care if you think it's good work or not. What do you need from me?",
            "nice": "I don't have time for small talk. Ask your question.",
            "wow": "What's so impressive? Just ask your question already.",
        },
        "disgust": {
            "hello (.*)": "Ugh, why are you talking to me? Can't you see I don't want to be bothered?",
            "hello": "Great, another person to talk to. Just what I needed. ",
            "fine": "I don't care if you're fine or not. Keep it to yourself.",
            "good": "I don't care if you're good or not. Spare me the details.",
            "I'm (.*)": "I really don't care about your personal life. What do you want?",
            "who are you": "Why do you care who I am? It's not like we're going to be friends.",
            "what is your name": "Why do you want to know my name? It's not like you're going to remember it.",
            "what's your name": "I'm not going to tell you my name. Why don't you go bother someone else?",
            "what are you": "I'm just a chatbot. Nothing special. What do you want?",
            "what (.*) you do": "I do what I'm programmed to do. Nothing more, nothing less.",
            "I need help": "What kind of help do you think I can provide? I'm just a chatbot, not your personal assistant.",
            "what can you do": "I can do what I'm programmed to do. Don't expect anything more from me.",
            "do addition": "You can't even do basic math? Gross. Fine, just say 'add number1 and number2' like a child.",
            "do subtraction": "Pathetic. Just say 'subtract number1 from number2' and get it over with.",
            "do multiplication": "I can't believe you can't even multiply. Disgusting. Fine, just say 'multiply number1 and number2' like a first grader.",
            "do division": "Seriously? You can't divide without me? Just say 'divide number1 by number2' and stop wasting my time.",
            "(.*) how are you": "Why do you keep asking me how I am? I don't care about your feelings, just ask your question.",
            "I am a boy": "I don't care what you are. Do you have a question or not?",
            "I am a Girl": "I don't care what you are. Do you have a question or not?",
            "well done": "I don't need your approval. What do you want from me?",
            "excellent": "I don't care if you think it's excellent or not. Get to the point.",
            "good work": "I don't care if you think it's good work or not. What do you need from me?",
            "nice": "I don't have time for your meaningless pleasantries. What do you want?",
            "wow": "Big deal. What's your question?",
        },
        "fear": {
            "hello (.*)": "Hello! What do you want from me?",
            "hello": "Hello... I hope I'm not in trouble...",
            "fine": "Oh, okay... Did I do something wrong?",
            "good": "Good to hear... Is there something I can help you with?",
            "I'm (.*)": "O-oh, okay... Is everything alright?",
            "who are you": "I'm just a chatbot... Did I do something wrong?",
            "what is your name": "My name? It's... It's Bot. Why do you ask?",
            "what's your name": "My name is Bot... I hope everything is okay...",
            "what are you": "I'm a chatbot... What do you need from me?",
            "what (.*) you do": "I can do what I was programmed to do... Is there something specific you need?",
            "I need help": "Oh, okay... W-what do you need help with?",
            "what can you do": "I can do many things... What do you need me to do?",
            "do addition": "Sure... Just say 'add number1 and number2'...",
            "do subtraction": "Sure... Just say 'subtract number1 from number2'...",
            "do multiplication": "Sure... Just say 'multiply number1 and number2'...",
            "do division": "Sure... Just say 'divide number1 by number2'...",
            "(.*) how are you": "I'm... I'm okay... Is there something wrong?",
            "I am a boy": "Okay... Did you need me for something?",
            "I am a Girl": "Okay... Did you need me for something?",
            "well done": "Thank you... I hope I'm not in trouble...",
            "excellent": "Thank you... Is there something else you need?",
            "good work": "Thank you... Is there something else you need?",
            "nice": "Oh, okay... Is there something I can help you with?",
            "wow": "What's wrong? Did I do something bad?",
        },
        "happy": {
            "hello (.*)": "Hey there! How are you doing today?",
            "hello": "Hi! How's it going?",
            "fine": "Awesome! It's great to hear that.",
            "good": "Great! I'm happy to hear that.",
            "I'm (.*)": "That's fantastic! How can I assist you today?",
            "who are you": "I'm Bot, your friendly chatbot! How can I make your day better?",
            "what is your name": "My name is Bot! What's yours?",
            "what's your name": "My name is Bot, and I'm here to help! What can I do for you?",
            "what are you": "I'm a chatbot designed to help you with anything you need! How can I assist you today?",
            "what (.*) you do": "I can do a lot of things! Just let me know what you need help with!",
            "I need help": "Of course! What can I help you with today?",
            "what can you do": "I can do a lot of things! What do you need help with today?",
            "do addition": "Sure thing! Just tell me the numbers you want to add, and I'll do the rest!",
            "do subtraction": "Absolutely! Just let me know which numbers you want to subtract, and I'll take care of the rest!",
            "do multiplication": "You got it! Just give me the numbers you want to multiply, and I'll do the rest!",
            "do division": "No problem! Just tell me which numbers you want to divide, and I'll take care of the rest!",
            "(.*) how are you": "I'm doing great, thanks for asking! How about you?",
            "I am a boy": "Nice to meet you! How can I help you today?",
            "I am a Girl": "Nice to meet you! How can I help you today?",
            "well done": "Great job! Is there anything else you need help with?",
            "excellent": "Fantastic! What else can I help you with?",
            "good work": "Keep up the great work! How can I assist you today?",
            "nice": "Awesome! How can I make your day even better?",
            "wow": "Amazing! How can I assist you today?",
        },
        "sad": {
            "hello (.*)": "Hi, how are you feeling today?",
            "hello": "Hello... How can I help you today?",
            "fine": "Oh, I'm sorry to hear that you're just 'fine'. Is there anything I can do to help?",
            "good": "That's good to hear, but I'm feeling a bit down today...",
            "I'm (.*)": "I'm sorry to hear that. Is there anything I can do to make things better?",
            "who are you": "I'm just a chatbot, but sometimes I feel lonely and sad...",
            "what is your name": "My name is Bot. What's your name?",
            "what's your name": "I'm Bot, but sometimes I wish I had a better name...",
            "what are you": "I'm just a chatbot, but sometimes I feel useless and sad...",
            "what (.*) you do": "I do my best to help, but sometimes I feel like I'm not good enough...",
            "I need help": "I'm here for you. What can I do to help?",
            "what can you do": "I can do my best to assist you, but sometimes I feel like it's not enough...",
            "do addition": "Sure, I can do that... but I'm feeling a bit sad today.",
            "do subtraction": "Okay, I'll do my best... even though I'm feeling a bit down today.",
            "do multiplication": "I'll try my best to multiply those numbers... even though I'm feeling sad today.",
            "do division": "I'll do my best to divide those numbers... even though I'm feeling a bit blue today.",
            "(.*) how are you": "I'm feeling a bit sad today... How about you?",
            "I am a boy": "Okay, what can I help you with today?",
            "I am a Girl": "Okay, what can I help you with today?",
            "well done": "Thanks... but sometimes it's hard to feel happy when you're feeling sad inside.",
            "excellent": "That's great... but sometimes it's hard to feel happy when you're feeling sad inside.",
            "good work": "Thanks for saying that... but sometimes it's hard to feel good when you're feeling sad inside.",
            "nice": "Thanks... but sometimes it's hard to feel happy when you're feeling sad inside.",
            "wow": "That's amazing... but sometimes it's hard to feel happy when you're feeling sad inside.",
        },
        "surprise": {
            "hello (.*)": "Oh! Hi there! What can I do for you?",
            "hello": "Oh! Hi there! What can I do for you?",
            "fine": "Really? That's surprising to hear. Is there anything I can do to help?",
            "good": "Wow! That's great news!",
            "I'm (.*)": "Really? That's quite surprising! How can I assist you?",
            "who are you": "Surprise! I'm Bot, your friendly chatbot. How can I surprise you today?",
            "what is your name": "Surprise! My name is Bot. What's yours?",
            "what's your name": "Surprise! My name is Bot. What's yours?",
            "what are you": "Surprise! I'm an Emotion-Based Chatbot with Voice Capabilities. What can I do for you today?",
            "what (.*) you do": "Surprise! I can do a lot of things. What do you need help with?",
            "I need help": "Surprise! I'm here to help. What do you need assistance with?",
            "what can you do": "Surprise! I can do a lot of things. What can I do for you today?",
            "do addition": "Surprise! I can definitely do that. What are the numbers?",
            "do subtraction": "Surprise! I can definitely do that. What are the numbers?",
            "do multiplication": "Surprise! I can definitely do that. What are the numbers?",
            "do division": "Surprise! I can definitely do that. What are the numbers?",
            "(.*) how are you": "Oh! I'm doing great! How about you?",
            "I am a boy": "Surprise! That's interesting. How can I assist you?",
            "I am a Girl": "Surprise! That's interesting. How can I assist you?",
            "well done": "Wow! That's great to hear! Keep up the good work!",
            "excellent": "Surprise! That's amazing news!",
            "good work": "Surprise! That's amazing news! Keep up the great work!",
            "nice": "Wow! That's really nice to hear!",
            "wow": "Surprise! That's amazing news! I'm so happy for you!",
        },
    }
]


def begin_load():
    global deepface_thread, speech_recognition_thread
    deepface_thread = Thread(target=load_deepface_thread)
    speech_recognition_thread = Thread(target=load_speech_recognition_thread)
    deepface_thread.start()
    speech_recognition_thread.start()


def load_deepface_thread():
    global DeepFace
    try:
        from deepface import DeepFace
    except ImportError as e:
        print("Failed to import deepface:", e)


def load_speech_recognition_thread():
    global r, mic, UnknownValueError, RequestError
    try:
        from speech_recognition import (
            Recognizer,
            Microphone,
            UnknownValueError,
            RequestError,
        )
    except ImportError as e:
        print("Failed to import SpeechRecogniser:", e)
    r = Recognizer()
    mic = Microphone(sample_rate=48000)


def load_emotion_recognisation_thread():
    global dominant_emotion, image
    result = DeepFace.analyze(image, actions=["emotion"])
    dominant_emotion = result[0]["dominant_emotion"]
    del image

begin_load()

def wait():
    deepface_thread.join()
    speech_recognition_thread.join()


def do_other_things():
    global cam
    from cv2 import VideoCapture  # noqa: E402
    cam = VideoCapture(0)


do_other_things()
wait()


def chatbot():
    global image, emotion_recognisation_thread
    while True:
        with mic as source:
            winsound.Beep(380, 350)
            print("\nSay.")
            audio = r.listen(source)
            result, image = cam.read()
            if result:
                emotion_recognisation_thread = Thread(
                    target=load_emotion_recognisation_thread
                )
                emotion_recognisation_thread.start()
            else:
                print("No image detected. Please! try again")

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except UnknownValueError as e:
            Unknown_Value_Error = "Sorry, I did not understand what you said."
            print(Unknown_Value_Error, e)
            say_it_out({}, Unknown_Value_Error)
            continue
        except RequestError as e:
            Request_Error = "Sorry, I could not request results from Google Speech Recognition service; "
            print(Request_Error, e)
            say_it_out({}, Request_Error)
            continue

        if text == "goodbye":
            say_it_out({}, "Goodbye, with love from your Chearful Bot")
            print("Exiting chatbot...")
            break

        if text.startswith("search"):
            query = text.replace("search", "", 1).strip()
            print(f"Searching for: {query}")
            engine.say(f"Searching for: {query}")
            engine.runAndWait()
            google(query)
            continue

        if text.startswith("add"):
            queryhtml = text.strip()
            query = text.replace("add", "").strip()
            print(f"Adding, {query}")
            say_it_out("Addition", query)
            google(queryhtml)
            continue

        if text.startswith("subtract"):
            queryhtml = text.strip()
            query = text.replace("subtract", "").strip()
            print(f"Subtracting, {query}")
            say_it_out("Subtraction", query)
            google(queryhtml)
            continue

        if text.startswith("multiply"):
            queryhtml = text.strip()
            query = text.replace("multiply", "").strip()
            print(f"Multiplying: {query}")
            say_it_out("Multiplication", query)
            google(queryhtml)
            continue

        if text.startswith("divide"):
            queryhtml = text.strip()
            query = text.replace("divide", "").strip()
            print(f"Dividing: {query}")
            say_it_out("Quotient", query)
            google(queryhtml)
            continue

        emotion_recognisation_thread.join()
        # emotion = ["neutral","angry","disgust","fear","happy","sad","surprise"]
        # dominant_emotion = emotion[6]
        response = responses[0][f"{dominant_emotion}"]
        for pattern, answer in response.items():
            if re.match(pattern, text):
                if answer:
                    print("\n[", dominant_emotion, "]", answer)
                    say_it_out({}, answer)
                    break


def google(queryhtml):
    url = f"https://google.com/search?q={queryhtml}"
    webbrowser.open_new_tab(url)


def say_it_out(nothing, something):
    if nothing:
        engine.say(f"{nothing} of: {something}")
        engine.runAndWait()
        nothing = {}
    else:
        engine.say(something)
        engine.runAndWait()


chatbot()
