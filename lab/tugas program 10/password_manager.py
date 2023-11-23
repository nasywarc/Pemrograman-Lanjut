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

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_usn_label = Label(text='Email/Username:')
email_usn_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)