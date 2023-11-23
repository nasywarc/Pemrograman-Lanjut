from tkinter import *

BLACK = '#000'
WHITE = '#FFF'

window = Tk()

window.title('Password Manager')
window.minsize(width=300, height=300)

my_label = Label(text='Lorem Ipsum', font=(20), fg=BLACK)
my_label.pack()


window.mainloop()