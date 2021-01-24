## Coded by Samuel Ayomide Ogunleke
## HSSP World
## Do not copy without permission
import sounddevice as sd
from scipy.io.wavfile import write
#from chatterbot import ChatBot
import wavio as wv
import numpy as np
import pyautogui
import cv2
import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
##from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id) 



def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def greet(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Dailex") 
    speak("I am Dailex, your virtual Assistant")       
  
  
def takeCommand(): 
      
    r = sr.Recognizer() 
    
    with sr.Microphone() as source: 
        speak("please say your command")
##        print("Listening...") 
        r.pause_threshold = 0.5
        speak("I am now Listening")
        print("Listening...")
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language = 'en') 
        print(f"Your command is: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to recognize your voice.")
        speak("I am sorry, I am unable to understand your command")
        return "None"
      
    return query 
   
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('your email id', 'your email password') 
    server.sendmail('your email id', to, content) 
    server.close() 



def soundRecorder():
    speak("for how many minutes do you want me to record")
    duration = float(input(">>> "))
    speak("sound recorder started")
    freq = 44100
    duration = 60 * duration
    recording = sd.rec(int(duration * freq), samplerate = freq, channels = 1)
    sd.wait()
    write("recording0.wav", freq, recording)
    speak("recording saved as a wav file")



def screenRecorder():
    speak("for how many minutes do you want me to record your screen")
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = "Dailex_screen_recorder.avi"
    fps = 60.0
    out = cv2.VideoWriter(filename, codec, fps, (resolution))
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("Screenshot", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()
    out.release()
    speak("recording saved as an AVI file")
        







    
if __name__ == '__main__': 
    #clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file 
    #clear() 
    greet()  
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak(" Redirecting you to Youtube dot com\n") 
            webbrowser.open("www.youtube.com") 
  
        elif 'open google' in query: 
            speak("Redirecting you to Google dot com\n") 
            webbrowser.open("www.google.com") 
  
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            # music_dir = "G:\\Song" 
            music_dir = r"C:\Users\hp\Desktop\recording0"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 
  
        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"Sir, the time is {strTime}") 
  
        elif 'open opera' in query: 
            codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
            os.startfile(codePath) 
  
        elif 'email to Praise' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "Receiver email address"    
                sendEmail(to, content) 
                speak("Email has been sent!") 
            except Exception as e: 
                print(e) 
                speak("I am sorry, I am not able to send this email") 
  
        elif 'send email' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("to whom do you want me to send the mail") 
                to = input("To: ")     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that you are fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  

        elif "what's your name" in query or "What is your name" in query or "your name" in query: 
            speak("I am DAILEX") 
            print("I am Dailex") 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:  
            speak("I have been created by Samuel.") 
              
        elif 'joke' in query or "jokes" in query or "tell me a joke" in query or "tell me some jokes" in query or "tell a joke" in query:
            speak("bringing you jokes")
            speak(pyjokes.get_joke()) 
              
        elif "calculate" in query:  
            speak("working on the problem")  
            app_id = "Wolframalpha api id" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query or 'play' in query: 
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)

        elif "browse for" in query and "dot" in query and "www" not in query and "come" in query:
            query = query.replace("browse for", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            query = query.replace("come", "com")
            webbrowser.open(query)

        elif "browse for" in query and "dot" in query and "www" in query and "come" in query:
            query = query.replace("browse for", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            query = query.replace("come", "com")
            webbrowser.open(query)

        elif "browse" in query and "browse for" not in query and "dot" not in query and "www" not in query and "come" not in query:
            query = query.replace("browse", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            webbrowser.open(query)

        elif "browse" in query and "browse for" not in query and "dot" in query and "www" in query and "come" in query:
            query = query.replace("browse", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            query = query.replace("come", "com")
            webbrowser.open(query)

        elif "browse for" in query and "dot" in query and "www" not in query and "come" not in query:
            query = query.replace("browse for", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            webbrowser.open(query)

        elif "browse for" in query and "dot" in query and "www" in query and "come" not in query:
            query = query.replace("browse for", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            webbrowser.open(query)

        elif "browse" in query and "browse for" not in query and "dot" not in query and "www" not in query and "come" not in query:
            query = query.replace("browse", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            webbrowser.open(query)

        elif "browse" in query and "browse for" not in query and "dot" in query and "www" in query and "come" in query:
            query = query.replace("browse", "")
            query = query.replace(" ", "")
            query = query.replace("dot", ".")
            query = query.replace("come", "com")
            webbrowser.open(query)
     
        elif "who i am" in query: 
            speak("If you have a heart and you breathe, you are human.") 
  
        elif "why were you created" in query or "why were you made" in query or "why did you come into the world" in query or "why you came to the world" in query: 
            speak("It's a secret, thanks to Samuel AYOMIDE") 
  
        elif "who are you" in query: 
            speak("I am Dailex, your virtual assistant") 
  
        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
            speak("Background changed succesfully") 
  
        elif 'news' in query: 
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-punch-nigeria&sortBy = top&apiKey =\\times of Nigeria Api key\\''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the punch, nigeria') 
                print('''=============== THE PUNCH, NIGERIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock my phone' in query or "lock this phone" in query: 
                speak("locking your device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown' in query or "switch off my phone" in query or "shutdowm my phone" in query: 
                speak("Switching off your phone") 
                subprocess.call('shutdown / p /f') 
                  
        elif "stop listening" in query or "do not listen" in query or "don't listen" in query: 
            speak("for how much time do you want me to stop taking commands, in seconds") 
            a = int(takeCommand(">>>")) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            location = query 
            speak("You asked for the location of") 
            speak(location) 
            webbrowser.open("https://www.google.nl / maps / place/" + location + "") 
  
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Dailex_snapshot", "img.png") 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('Dailex.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show notes" in query or "show my notes" in query: 
            speak("Showing Notes") 
            file = open("Dailex.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
  

        elif "Dailex" in query: 
            greet() 
            speak("Dailex at your service") 
  
        elif "what is the weather" in query or "tell me the weather" in query or "what's the weather" in query or "weather" in query: 
            ## Google Open weather website 
            ## to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found, sorry ") 
              
        elif "send message " in query: 
                # You need to create an account on Twilio to use this service 
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token) 
  
                message = client.messages.create( \
                                    body = takeCommand(), 
                                    from_='Sender No', 
                                    to ='Receiver No'
                                ) 
  
                print(message.sid) 
  
        elif "wikipedia" in query: 
            webbrowser.open("wikipedia.com") 
  
        elif "Good Morning" in query: 
            speak("A pleasant morning to you there")

        elif "Good Afternoon" in query: 
            speak("A warm noon to you there")

        elif "Good Evening" in query: 
            speak("A pleasant evening to you there")

        elif "Good Night" in query: 
            speak("Good night, sweet dreams")

        # Some silly questions asked by some users
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm a robot, I can only be your friend") 
  
        elif "how are you" in query: 
            speak("I'm fine, thank you") 
  
        elif "i love you" in query: 
            speak("I'm not allowed to reply to this")
  
        elif "what is" in query or "who is" in query: 
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")


        elif "start voice recorder" in query or "start sound recorder" in query:
            soundRecorder()

        elif "start screen recorder" in query:
            screenRecorder()
        # elif "" in query: 
            # Commands here... 
            # For adding more commands 
       # else:
        #    webbrowser.open(query)
#
##
###
####
#####
######
#######
########
#########
##########
###########
############
#############
##############
###############





