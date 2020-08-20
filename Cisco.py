import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import smtplib
import wikipedia
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def jokes():
    speak(pyjokes.get_jokes())


def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at " + usage)

    battery = psutil.sensors_battery()
    speak("battery is at ")
    speak(battery.percent)


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is ")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("welcome back sir!!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour <= 24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("Cisco at your service. How can i help you sir!")


def Take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, "en-US")
        print(query)
    except Exception as e:
        print(e)
        speak("Please try saying that again!....")

        return "None"

    return query


# if __name__ == "__main__":

#     wishme()

#     while True:
#         query = Take().lower()
#         print(query)

#         if "time" in query:
#             time()
#         elif "date" in query:
#             date()
#         elif "offline" in query:
#             quit()
#         elif "search chrome for" in query:
#             speak("What should i search for sir?")
#             chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
#             search = Take().lower()
#             wb.get(chromepath).open_new_tab(search + ".com")
#         elif "logout" in query:
#             os.system("Shutdown - 1")
#         elif "shutdown" in query:
#             os.system("Shutdown /s /t 1")
#         elif "restart" in query:
#             os.system("Shutdown /r /t 1")
#         elif "play song" in query:
#             song_dir = "C:\Users\96657\Music\quran"
#             songs = os.listdir(song_dir)
#             os.startfile(os.path.join(song_dir, songs[0]))
#         elif "remeber that" in query:
#             speak("what should i remeber")
#             data = Take()
#            speak("You asked me to remeber " + data)
#            remeber = open.("data.txt","w")
#            remeber.write(data)
#          remeber.close()
#     elif "my memory" in query:
#         remeber = open("data.txt","r")
#        speak("I was asked to remember " remeber.read() )
#     elif "screeschot" in query:
#         Sshot()
#         speak("taking a screeshot....Completed!")--also if this doesnt work move the
#          sshot command above this command.
#   if you want to add a command voice related you have to an elif that searches if something
#    is in a query


def play_Song():
    song_dirz = "C:\\Users\\96657\\Music\\quran"
    songz = os.listdir(song_dirz)
    os.startfile(os.path.join(song_dirz, songz[0]))


def Sshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\96657\\Desktop\\Jarvis\\jarvis shots\\firstimage.png")
    speak("Taking a screenshot")
    speak("completed the screenshot!")


#not complete left still have to do email and wiki search but good work up till here.