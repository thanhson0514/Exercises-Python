import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

def speaknow():
    engine.say(txtv.get())
    engine.runAndWait()
    engine.stop()

root = Tk()

txtv = StringVar()

wrapper = LabelFrame(root, text="Text to Speech")
wrapper.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(wrapper, text="Text")
lbl.pack(side=tk.LEFT, padx=10)

txt = Entry(wrapper, textvariable=txtv)
txt.pack(side=tk.LEFT, padx=5)

btn = Button(wrapper, text="speak", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

root.title("Text to Speech")
root.geometry('350x100')
root.resizable(False, False)
root.mainloop()