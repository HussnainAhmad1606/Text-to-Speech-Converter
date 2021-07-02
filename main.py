'''
Program: Text to Speech Converter

Coder: HUSSNAIN AHMAD

Date: 24-06-2021
'''

import pyttsx3
from tkinter import *
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Change index of voices below to change voice
# 0 --> Man
# 1 --> Woman
engine.setProperty('voice', voices[1].id)


def speakText():
    audio = userText.get()
    engine.say(audio)
    engine.runAndWait()


root = Tk()
root.title("Text to Speech Converter")

root.geometry("300x140")

frame = Frame(root, bg="grey", padx=40, pady=20, borderwidth=10, relief=SUNKEN)
frame.pack()

title = Label(frame, text="Enter text to Speak", bg="grey", fg="white", font=("Berlin Sans FB", 18))
title.grid(column=0, row=1)

userText = StringVar()

userEntry = Entry(frame, textvariable=userText)
userEntry.grid(column=0, row=2)

convertBtn = Button(frame, text="Convert", command=speakText, pady=5)
convertBtn.grid(column=0, row=4)

root.mainloop()
