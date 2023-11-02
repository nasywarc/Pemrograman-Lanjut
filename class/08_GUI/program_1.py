import tkinter

tk = tkinter.Tk()
# tk.title('New Window')
# tk.mainloop()

# tk.title('Canvas')
# canvas = tkinter.Canvas(tk, width=300, height=300)
# canvas.grid()
# tk.mainloop()

# tk.title('Button')
# button = tkinter.Button(tk, text='Simpan', width=30, command=tk.destroy, background='black')
# button.pack()
# tk.mainloop()

tk.title('CheckButton')
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
C1 = tkinter.Checkbutton(tk, text='Laki - laki', variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
C2 = tkinter.Checkbutton(tk, text='Perempuan', variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)

C1.pack()
C2.pack()
tk.mainloop()