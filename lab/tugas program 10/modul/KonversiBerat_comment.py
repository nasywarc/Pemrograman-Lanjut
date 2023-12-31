# Nasywa Azizah Zharifah
# 225150307111060

from tkinter import *

# membuat window sebagai object tkinter
window = Tk()

# fungsi untuk mengonversi berat
def from_kg():
    # mengonversi kg ke gram
    gram = float(e2_value.get())*1000
    # mengonversi kg ke pound
    pound = float(e2_value.get())*2.20462
    # mengonversi kg ke ons
    ounce = float(e2_value.get())*35.274
    
    # widget teks
    t1.delete("1.0", END)
    t1.insert(END,gram)
    
    t2.delete("1.0", END)
    t2.insert(END,pound)
    
    t3.delete("1.0", END)
    t3.insert(END,ounce)
    
# membuat Label widget
e1 = Label(window, text = "Enter the weight in Kg")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = 'Gram')
e4 = Label(window, text = 'Pounds')
e5 = Label(window, text = 'Ounce')
    
# membuat Text widget
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)

# membuat Button widget
b1 = Button(window, text = "Convert", command = from_kg)

# mengatur struktur kolom dan baris (grid)
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)
b1.grid(row = 0, column = 2)
    
# menjalankan window untuk di-looping
window.mainloop()
