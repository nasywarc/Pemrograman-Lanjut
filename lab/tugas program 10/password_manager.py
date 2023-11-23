from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

BLACK = '#00F' # 000
WHITE = '#FF0' # FFF

window = Tk()

window.title('Password Manager')
window.minsize(width=400, height=300)

my_label = Label(text='This is Password Manager', font=(20), fg=BLACK)
my_label.pack()


window.mainloop()