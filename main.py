import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia
import instaloader

import phonenumbers as pn
from phonenumbers import carrier,geocoder,timezone

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
female_voice = engine.setProperty("voice", voices[1].id)

engine.say("Hello Sir, I am your assistant.")
engine.say("What can i do for you?")
engine.runAndWait()


def speak(input):
    engine.say(input)
    engine.runAndWait()


def speak1(input, abc):
    engine.say(input)
    engine.say(abc)
    engine.runAndWait()


def input_command():
    with sr.Microphone() as source_input:
            speak("Listening to your command.....")
            print("Listening to your command.....")
            voice_input = listener.listen(source_input)
            try:
                command = listener.recognize_google(voice_input)
                command = command.lower()
                if 'dodo' in command:
                    command = command.replace('dodo', '')
                    print(command)
            except:
                print("Sorry could not recognize what you said.")
            return command


def run_dodo():
    command = input_command()
    command = command.replace("alexa", "")
    print(command)
    if 'play' in command:
        song = command.replace("play", "")
        speak("Playing" + song)
        print("playing" + song + "on youtube")
        pywhatkit.playonyt(song)
    elif "what can you do" in command:
        speak("Trying to check me? OK!")
        speak("I can play a youtube video, do a google search, tell a joke annnd by the way some secret stuff like tell details of a number. surrrprised!")
    elif 'search' in command:
        search_element = command.replace("search", "")
        speak("Searching " + search_element)
        print("Searching " + search_element + "on google")
        pywhatkit.search(search_element)
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        speak(jokes)
        print(jokes)
    elif "on wikipedia " in command:
        find = command.replace('on wikipedia', '')
        info = wikipedia.summary(find, 1)
        print(info)
        speak(info)
    elif "tell me about a number" in command:
        speak("OK tell me the number with country code. ")
        mob_num = input("Enter the number with country code: ")
        speak("The number entered is " + str(mob_num))
        mob_num = pn.parse(mob_num)
        valid = pn.is_valid_number(mob_num)
        if valid == True:
            speak("The number entered is a valid number.")
            print("The country is ", geocoder.description_for_number(mob_num, "en"))
            speak1("The country is ", geocoder.description_for_number(mob_num, "en"))
            print("The country and time zone is ", timezone.time_zones_for_number(mob_num))
            speak1("The country and time zone is ", timezone.time_zones_for_number(mob_num))
            print("The carrier is ", carrier.name_for_number(mob_num, "en"))
            speak1("The carrier is ",carrier.name_for_number(mob_num, "en"))
        else:
            speak("The number entered is Not valid. ")
    elif "download instagram dp" in command:
        speak("Please enter the insta username")
        ig = instaloader.Instaloader()
        dp = input("Enter insta username: ")
        ig.download_profile(dp,profile_pic_only=True)
    else:
        pywhatkit.search(command)

run_dodo()