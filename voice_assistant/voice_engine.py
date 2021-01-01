import speech_recognition as sr
import pyttsx3
import sys


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.setProperty('rate', 160)

engine.say(sys.argv[1])
engine.runAndWait()