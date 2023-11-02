import tkinter

tk = tkinter.Tk()
# tk.title('New Window')
# tk.mainloop()

# tk.title('Canvas')
# canvas = tkinter.Canvas(tk, width=300, height=300)
# canvas.grid()
# tk.mainloop()

tk.title('Button')
button = tkinter.Button(tk, text='Simpan', width=30, command=tk.destroy)
button.pack()
tk.mainloop()