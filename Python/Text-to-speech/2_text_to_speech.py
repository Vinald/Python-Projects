import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# Function to convert text to speech
def convert():
    text = entry.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to save the converted text to speech
def save():
    text = entry.get()
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

# Function to open a file
def open_file():
    file = filedialog.askopenfilename()
    with open(file, 'r') as f:
        entry.insert(0, f.read())

# Function to save the text to a file
def save_file():
    text = entry.get()
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return
    file.write(text)
    file.close()

# Function to clear the text
def clear():
    entry.delete(0, END)
    
# Function to exit the application
def exit():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title('Text to Speech')
window.geometry('500x500')

# Create a label
label = Label(window, text='Enter the text:')
label.pack()

# Create an entry widget
entry = Entry(window, width=50)
entry.pack()

# Create a button to convert the text to speech
button1 = Button(window, text='Convert', command=convert)
button1.pack()

# Create a button to save the converted text to speech
button2 = Button(window, text='Save', command=save)
button2.pack()

# Create a button to open a file
button3 = Button(window, text='Open', command=open_file)
button3.pack()

# Create a button to save the text to a file
button4 = Button(window, text='Save File', command=save_file)
button4.pack()

# Create a button to clear the text
button5 = Button(window, text='Clear', command=clear)
button5.pack()

# Create a button to exit the application
button6 = Button(window, text='Exit', command=exit)
button6.pack()

# Run the main loop

window.mainloop()
cdll Creates ()