import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
        alexa.say(text)
        alexa.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='EN')
            print(f"User said: {query}\n")

    except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
    return query

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
            look_for = command.replace('tell me about', '')
            info = wikipedia.summary(look_for, 1)
            print(info)
            talk(info)
    elif 'joke' in command:
            talk(pyjokes.get_joke())
    elif 'date' in command:
            talk('Sorry via, I am in another relation')
    elif 'how are you' in command:
        talk('i am fine and you?')

    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)

    while True:
        run_alexa()


import tkinter as tk
from tkinter import *
from tkinter import ttk


class MHRS( Frame ):
    def __init__(self):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("VIRTUAL ASSISTANT")
        self.button1 = Button( self, text = "SPEAK", width = 25,command =take_command)
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    # def new_window(self):
    #     self.newWindow = karl2()
# class karl2(Frame):
#     def __init__(self):
#         new =tk.Frame.__init__(self)
#         new = Toplevel(self)
#         new.title("karlos More Window")
        self.button2 = tk.Button(self, text = "PRESS TO CLOSE", width = 25,command=)
        self.button2.grid( row = 1, column = 1, columnspan = 3, sticky = W+E+N+S )

    # def close_window(self):
    #     self.destroy()
def main():

    MHRS().mainloop()
if __name__ == '__main__':
    main()

#,command = self.new_window command = self.close_window