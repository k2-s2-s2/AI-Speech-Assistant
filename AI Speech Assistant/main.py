import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning All")
    elif hour>=12 and hour<4:
        speak("Good Afternoon All")
    else:
        speak("Good Evening All")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening.....Kindly Talk")
         r.pause_threshold=1
         audio=r.listen(source)
    try:
        print("recognizing....your Voice")
        query=r.recognize_google(audio,language='en-in')
        print("user Said: ", query)
    except Exception as e:
           print(e)
           speak("Soory, I cant here you, you voice is not audible please Repeat again")
           return "none"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        speak("How can i help you Today?")
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
             webbrowser.open("youtube.com")
             speak("youtube is opened")
        elif 'open google' in query:
             webbrowser.open("google.com")
             speak("google is opened")
        elif 'open gmail' in query:
             webbrowser.open("gmail.com")
             speak("gmail is opened")
        elif 'youtube music' in query:
             webbrowser.open("music.youtube.com")
             speak("Youtube Music is opened")
        elif 'play music' in query:
              music_dir='D:\songs'
              songs=os.listdir(music_dir)
              print(songs)
              os.startfile(os.path.join(music_dir, songs[0]))
              speak("Music playing Enjoy")
        elif 'time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"the time is {strTime}")

        elif 'open voter code' in query:
             codepath="C:\\Users\\shiva\\PycharmProjects\\pythonProject\\voter.py"
             os.startfile(codepath)
             speak("Your requested project code is Running")

        elif 'exit' in query:
            speak("See you soon, take care")
            exit()
        else:
            webbrowser.open(query)

