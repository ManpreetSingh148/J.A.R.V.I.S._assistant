import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib 
import playsound
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:

        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am JARVIS your personal assistant. How may I help you?")    

def takeCommand():
    #It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    sever.ehlo()
    sever.startttls()
    sever.login('testimonal.0718@gmail.com', '9832944001')
    sever.sendemail('testimonal.0718@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url = 'https://www.youtube.com/?gl=IN&tab=r10&authuser=0'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure Sir! Loading Page")

        elif 'open google' in query:
            url = 'https://www.google.com/webhp?authuser=1'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Loading Sir! \n\n Go ahead and search out")

        elif 'open stack overflow' in query:
            url = 'https://stackoverflow.com/users/13195785/manpreet-singh?tab=tags'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir! Just a second while the page loads up!")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\computer\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Yes Sir! It is good to hear music when you are pissed off!")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'programming' in query:
            codePath = "C:\\Users\\computer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Sure Sir. Just a minute")

        elif 'an email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "singhs_garage@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, but we got some problem out there coz' we are offline")

        elif 'my inbox' in query:
            url = 'https://mail.google.com/mail/?tab=rm0&authuser=0&ogbl'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir. Checking for the latest mails. Just a minute")

        elif 'play games' in query:
            codePath = "D:\\Call of Duty Black Ops"
            os.startfile(codePath)
            speak("Sure Sir. Just a minute. I hope you enjoy your game and cross the last mission!")

        elif 'open whatsapp' in query:
            url = 'https://web.whatsapp.com/'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir. Just a minute while it opens. Make sure your primary device is connected to it")

        elif 'workout' in query:
            codePath = "C:\\Users\\computer\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
            speak("Sure Sir. Just a minute. Make sure you break your last record! And make sure that your muscles burn!")

        elif 'a reminder' in query:
            try:
                print("What should I make a note of?")
                speak("What should I make a note of?")
                content = takeCommand()
                url = 'https://calendar.google.com/calendar/r'
                webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
                webbrowser.get('chrome').open(url)
                makeNote(url, content)
                speak("Alright sir. It's done!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, can you please repeat it!")

        elif 'do exercise' in query:
            codePath = "C:\\Users\\computer\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
            speak("Sure Sir. Just a minute. Make sure you break your last record! And make sure that your muscles burn!")

        elif 'coding' in query:
            codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
            speak("Sure Sir. But I am in a constant fear that you will build someone better than me!")

        elif 'weather' in query:
            url = 'https://www.theweathernetwork.com/in/weather/jharkhand/barakar'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure Sir! Checking the enviroment around you")

        elif 'open udemy' in query:
            url = 'https://www.udemy.com/?utm_source=adwords-brand&utm_medium=udemyads&utm_campaign=Brand-Udemy_la.EN_cc.INDIA&utm_term=_._ag_78279294239_._ad_387461093429_._de_c_._dm__._pl__._ti_kwd-310556426868_._li_20472_._pd__._&utm_term=_._pd__._kw_udemy_._&matchtype=e&gclid=CjwKCAjwhOD0BRAQEiwAK7JHmP9McFi-CU7THJNYU-ofxdE2Sjajz1rpMsnYME2GwlkepvkXXBQFkBoC-qEQAvD_BwE'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir! Make sure you learn something exciting!")

        elif 'open hotstar' in query:
            url = 'https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjn26rz3KbpAhVSPmAKHQ3yDbgYABAAGgJ0bQ&ohost=www.google.com&cid=CAESP-D2fJVDmXep-ctMluKRF44XyU1XRElOCDsN1mX3BNzOeash6yvFo0QPr8P_GzzzF3nQ8cpH4_oMvIYyIl_vWA&sig=AOD64_2kMuCa6oieSjyHWeN2TM6XeS0yVg&q=&ved=2ahUKEwifmqHz3KbpAhWazDgGHQYtCVAQ0Qx6BAgTEAE&adurl='
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir! By the way which series are you watching today! ")

        elif 'open github' in query:
            url = 'https://github.com/ManpreetSingh148'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir! ")

        elif 'open analytics' in query:
            url = 'https://studio.youtube.com/channel/UC_C6EXnWBy0eMCLAhx-unww'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir! Just a minute.  ")

        elif 'my analytics' in query:
            url = 'https://studio.youtube.com/channel/UCXTAj1XALsvwEL_QDsjcLwQ'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Sure sir! Just a minute.  ")

        elif 'status' in query:
            speak("Importing preferences.. Encalibrating Virtual enviroment. I have indeed been uploaded sir.. we are online and ready...At your service sir!")

        elif 'the responses' in query:
            url = 'https://docs.google.com/forms/d/1y6sRV3MJt0uKLpBsKoX7xAFhMS5zkEYknI5SJvSV0zs/edit'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url)
            speak("Working on it! Just a second.  ")

        elif 'go to sleep' in query:
            speak("As you wish Sir,   You can call me any time    \n\n\n\nI am always ready for you!")
            exit()

        elif 'hey jarvis' in query:
            speak("Yes Sir! Are there any orders")

        elif 'you there' in query:
            speak("For you Sir, Always!")

        elif 'sun jarvis' in query:
            speak("Ji Sir! Kyaa aapke paas mere liya koi order hai?")
