import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()


while True:
    try:
        with sr.Microphone() as source:
            print("say something to be transcribed ")
            audio = r.listen(source)
            text =r.recognize_google(audio)
            print("this is what you said {}".format(text))
    except sr.UnknownValueError():
        print("i didn't get you well")