from tkinter import *

BLACK = '#00F' # 000
WHITE = '#FF0' # FFF

window = Tk()

window.title('Password Manager')
window.minsize(width=400, height=300)

my_label = Label(text='Lorem Ipsum', font=(20), fg=BLACK)
my_label.pack()


window.mainloop()