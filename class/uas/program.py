# string1 = '     Halo     '
# string2 = 'Semua    '

# print(len(string1))
# print(len(string1.strip()))
# print(len(string2))
# print(len(string2.strip()))

# print(string1)
# print(string1.lstrip())
# print(len(string1.rstrip().lstrip()))
# print(len(string1.rstrip()))
# print(len(string2.rstrip()))


# a = 10
# print(a)
# a += int('10', 2)
# print(a)
# a += int('10', 8)
# print(a)
# a += int('0x10', 16)
# print(a)
# print(bin(2))

# string = 'pemrograman'
# print(string[-5:])
# print(string[-5:-3])

# # cara pertama
# file = open('contoh_file.txt', 'w')
# file.write('line satu')
# file.close()

# # cara kedua (lebih aman)
# with open('contoh_file.txt', 'a') as file:
#     file.write('\nline kedua')

from tkinter import *

def click_on_button():
    global iterate
    print(iterate)
    if iterate % 2 == 0:
        window.config(bg='#000')
    else:
        window.config(bg='#FFF')
    iterate += 1
    
iterate = 0
window = Tk()
window.title('New Window')
window.geometry('300x100')
window.config(padx=100, pady=30)

button1 = Button(text='Click This Button', command=click_on_button, activebackground='#8A383C', activeforeground='#FFF')
button1.grid(row=0, column=0)

window.mainloop()

