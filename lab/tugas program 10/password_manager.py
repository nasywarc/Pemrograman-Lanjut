from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

file_path = 'data.txt'

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)