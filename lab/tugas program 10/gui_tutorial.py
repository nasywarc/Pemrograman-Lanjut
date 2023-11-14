# # hello world program

# from tkinter import *

# root = Tk()

# # creatine a label widget
# myLabel = Label(root, text='Hello World!')
# # showing it onto the screen
# myLabel.pack()

# root.mainloop()


# grid program

from tkinter import *

root = Tk()

# creatine a label widget
myLabel1 = Label(root, text='Hello World!')
myLabel2 = Label(root, text='My Name Is John Elder!')
# showing it onto the screen

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()