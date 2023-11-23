from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

file_path = 'data.txt'

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)