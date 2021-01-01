import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from API.client import *

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.setProperty('rate', 160)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-IN')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('friday', '')
                print(command)
    except():
        pass
    return command


def run_friday():
    command = take_command()
    r_command = command.replace('friday ', '')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    # elif 'date' or 'day' in command:
    #     date = datetime.date.today().strftime('%A')
    #     talk('today is' + date)
    elif 'are you a robot' in command:
        talk('Consider me your friend')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'operate pin' in command or 'corporate pin' in command:
        pin = int(command[19:21])
        command = command.replace('friday ', '')
        if pin < 28 and pin not in [1, 14, 15]:
            if command.endswith('high') or command.endswith('hai'):
                digital_set_gpio(pin, 1)
                talk("Digital pin {} set to high".format(pin))
            if command.endswith('low') or command.endswith('lo'):
                digital_set_gpio(pin, 0)
                talk("Digital pin {} set to low".format(pin))

        run_friday()
    elif 'set analog pin' in command:
        command = command.replace('friday ', '')
        if len(command) >= 21:
            if command[15:17].isnumeric():
                pin = int(command[15:17])
            if command[20:].isnumeric():
                value = int(command[20:])
            if pin < 28 and pin not in [1, 14, 15]:
                analog_set_gpio(pin, value)
                talk("Analog Pin {} set to value : {}".format(pin, value))
        else:
            talk('Please say the command again.')
            run_friday()
    else:
        talk('Please say the command again.')
        run_friday()

    return r_command
