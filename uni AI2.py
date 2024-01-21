import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import wikipedia
import webbrowser
import pywhatkit
import sys
import time
import os
import os.path
import kit                
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from Dictapp import openappwed
from Dictapp import closeappwed
from gui import Ui_mainWindow
import pyautogui
import smtplib
engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)
QGestureRecognizer=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def greetme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon")
    else:
        speak(f"good evening")
    speak("I am U KNOW please tell me how may i help you")

def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ramanroy2003@gmail.com','eiwhysjceclfoebe')
    server.sendmail('ramanroy2003@gmail.com',to ,content)
    server.close()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def takecommand(self):
        r =sr.Recognizer()
        with sr.Microphone() as source:
        
            speak("listening...")
            r.pause_threshold = 1
            r.energy_threshold =300
            audio = r.listen(source,timeout=5,phrase_time_limit=8)
 
        try:
            
            print("understanding sir....")
            query =r.recognize_google(audio,language='en=in')
            print("user said:",{query})

        except Exception as e:
            print("say that again please....!")
            #speak("say that again please...")
            return "None"
        query = query.lower()
        return query

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        while True:
            self.query = self.takecommand().lower()
        
#wikipedia----------------------------------------------------------------------------           
            if "wikipedia" in self.query:
                speak("searching from Wikipedia....")
                query = self.query.replace("Wikipedia","")
                query = self.query.replace("search Wikipedia","")
                query = self.query.replace("uniAI","") 
                results =wikipedia.summary(query,sentences = 2)
                speak("According to wikipedia...")
                print(results)
                speak(results)
              
            
            elif "i am fine" in self.query:
                speak("that's great,sir")
            elif "thank you" in self. query:
                speak("you are welcome,sir that's my  pleasure")
#restart----------------------------------------------------------------------------------------------------                
            elif "restart the system" in self.query:
                 os.system("shutdown /r /t 5")
#shut down--------------------------------------------------------------------------------------------------                                
            elif "shut down the system" in self.query:
                 os.system("shutdown /s /t 5")
#search on youtube--------------------------------------------------------------------------------------                 
            elif "search youtube" in self.query:
                speak(" what i found for your search!")
                query = self.query.replace("youtube search"," ")
                query = self.query.replace("youtube "," ")
                query = self.query.replace("uniAI","")
                query = self.query.replace("play","")
                web ="https://www.youtube.com" + query 
                webbrowser.open(web)
                pywhatkit.playonyt(query)
                speak("done,sir")

            elif 'open' and 'youtube' in self.query: 
                webbrowser.open("https://www.youtube.com")
            elif 'open instagram' in self.query: 
                webbrowser.open("instagram.com")
            elif 'search' and 'google' in self.query: 
                webbrowser.open("google.com")
#google search----------------------------------------------------------------------------------------------------------                
            elif"google" in self.query:
                import wikipedia as googleScrap
                query = query.replace("uniAI","")
                query = query.replace("google search","")
                query =query.replace("google","")
                speak("what i found on google")
                try:
                    pywhatkit.search(query)
                    result =googleScrap.summary(query,1)
                    speak(result)
                except:
                    speak("no speakable output available")
            elif 'stack overflow' in self.query: 
                webbrowser.open("stackoverflow.com")
#exit------------------------------------------------------------------------------------------------------------
            elif 'exit' in self.query:
                speak("have  a nice day")
                break
            
#play music---------------------------------------------------------------------------------------------------------
            elif 'play music' in self.query:
                path ="https://www.jiosaavn.com//"+ self.query
                os.startfile(path)
                #pywhatkit.playonyt(query)
                speak("done,sir")
#tell the time-------------------------------------------------------------------------------------------------
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
#send email---------------------------------------------------------------- ---------------------------------------                   
            elif 'send' and 'email' in self.query:
                try:
                    speak("What should i say")
                    content =self.takecommand()
                    to ="22BCS80005@cuchd.in"

                    sendEmail(to,content)
                    speak("Email to Raman has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry ,i am not able to send this ")
#open whatsapp------------------------------------------------------------------------------------------------------------------                    
            elif 'open whatsapp' in self.query: 
                path ="https://web.whatsapp.com/"+ self.query
                os.startfile(path) 
                speak("done,sir")
            elif "open" in self.query:
        
                openappwed(self.query)

            elif "close" in self.query:
                closeappwed(self.query)

            elif "volume up" in self.query:
                from keyboard import volumeup
                speak("Turning volume up ,sir")
                volumeup()
            elif "volume down" in self.query:
                from keyboard import volumedown
                speak("Turning volume down ,sir")
                volumedown()
#play---------------------------------------------------------------------------------------------------------------------                
            elif "play" in self.query:
                pyautogui.press("k")
                speak("video play")
            elif "pause" in self.query:
                pyautogui.press("k")
                speak("video pause")
#mute-------------------------------------------------------------------------------------------------------------
            elif "mute" in self.query:
                pyautogui.press("m")
                speak("video mute")



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.start_button.clicked.connect(self.startTask)
        self.ui.quit_button.clicked.connect(self.close)
        self.ui.mic_button.clicked.connect(self.startTask2)
    def startTask2(self):
        startExecution.start()
    def startTask(self):
        self.ui.movie_5=QtGui.QMovie("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\wave.gif")
        self.ui.wave_label.setMovie(self.ui.movie_5)
        self.ui.movie_5.start()
        self.ui.movie2=QtGui.QMovie("C:\\Users\Home\\Desktop\\Personal voice assistant\\gif\\ball.gif")
        self.ui.ball_label.setMovie(self.ui.movie2)
        self.ui.movie2.start()
        greetme()
        startExecution.start()
        


app =QApplication(sys.argv)
uniAi2 =Main()
uniAi2.show()
exit(app.exec_())