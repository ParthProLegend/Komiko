import pyttsx3
import winsound
import webbrowser
from threading import Thread
import google.generativeai as genai

api_key_file = open("{api_key_relative_location}", "r").read()
genai.configure(api_key=f"{api_key_file}")
model = genai.GenerativeModel("gemini-pro")

operations = [
    {
        "add": "Addition",
        "subtract": "Subtraction",
        "multiply": "Multiplication",
    },
    {
        "add": "Sum",
        "subtract": "Difference",
        "multiply": "Product",
    },
]
engine = pyttsx3.init()


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
    from cv2 import VideoCapture

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
                emotion_recognisation_thread = Thread(target=load_emotion_recognisation_thread)
                emotion_recognisation_thread.start()
            else:
                print("No image detected. Please! try again")
                continue

        try:
            text = r.recognize_google(audio)
            # print(f"You said: {text}")
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

        if text.startswith("info"):
            query = text.replace("info", "", 1).strip()
            print(f"Some Information about {query} is as follows:\n")
            reply = model.generate_content(f"Give Trusted Sourced Information within for this: {query} ")
            answer = reply.text
            answer = (f"Some Information about {query} is as follows\n" + answer)
            answer = answer.replace("**", "").strip()
            answer = answer.replace("*", "").strip()
            print(f"\n {answer}")
            say_it_out({}, answer)
            continue

        if text.startswith("search"):
            query = text.replace("search", "", 1).strip()
            print(f"Opening {query} in a new tab.")
            say_it_out({},f"Opening {query} in a new tab.")
            google(query)
            continue

        if text.startswith(("add", "subtract", "multiply")):
            operation = text.split(" ", 1)[0]
            query = text.replace(f"{operation}", "").strip()
            reply = model.generate_content(f"{operation} these values and give just the answer: {query} ")
            answer = reply.text
            print(f"{operations[1][f"{operation}"]} of, {query}")
            print(f"\n The {operations[0][f"{operation}"]} of {query} is: {answer}")
            say_it_out(operations[0][f"{operation}"], query)
            say_it_out({},answer)
            continue

        if text.startswith("divide"):
            query = text.replace("divide", "").strip()
            reply = model.generate_content(f"Divide first value from the second value among these values and give just the quotient as value: {query} ")
            answer = reply.text
            print(f"Dividing: {query}")
            print(f"\n The Quotient of {query} is: {answer}")
            say_it_out("Quotient", query)
            say_it_out({},answer)
            continue

        emotion_recognisation_thread.join()
        reply = model.generate_content(f"While I am {dominant_emotion}, Give appropriate response to this: {text} ")
        answer = reply.text
        print("\n[", dominant_emotion, "]", answer)
        say_it_out({}, answer)


def google(queryhtml):
    url = f"https://google.com/search?q={queryhtml}"
    webbrowser.open_new_tab(url)


def say_it_out(nothing, something):
    if nothing:
        engine.say(f"{nothing} of {something} is:")
        engine.runAndWait()
        nothing = {}
    else:
        engine.say(something)
        engine.runAndWait()


chatbot()
