# Nasywa Azizah Zharifah
# 225150307111060

from random import choice, randint, shuffle # untuk generate password
from tkinter import * # untuk membuat GUI
from tkinter import messagebox # untuk menampilkan prompt messagebox
import pyperclip # untuk mengcopy ke clipboard

file_path = 'data.txt' # menginisialisasi file_path


# fungsi untuk generate password secara acak, berfungsi jika generate password diklik
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    # dalam range randint antara 8 sampai 10, memilih 1 huruf
    # dan memasukkannya ke dalam password_letters
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    # dalam range randint antara 2 sampai 4, memilih 1 simbol
    # dan memasukkannya ke dalam password_symbols
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # dalam range randint antara 2 sampai 4, memilih 1 angka
    # dan memasukkannya ke dalam password_numbers
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    
    # menggabungkan semua karakter password
    password_list = password_letters + password_symbols + password_numbers
    # mengacak urutan dari password_list
    shuffle(password_list)
    
    # memasukkan tiap string dalam list password_list ke var password
    password = "".join(password_list)
    # menginsertkan password ke dalam password_entry dari index 0
    password_entry.insert(0, password)
    # menggunakan pyperclip untuk copy ke clipboard
    pyperclip.copy(password)
    

# fungsi untuk memasukkan data yang user input ke data.txt    
def save():
    
    # jika entry kosong maka akan menampilkan messagebox warning
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(
            title='Oops', message='Please don\'t leave any fields empty!')
    else:

        is_ok = messagebox.askokcancel(title=website_entry.get(
        ), message=f'These are the details entered:\n\nWebsite:{website_entry.get()}\nEmail:{email_usn_entry.get()}\nPassword: {password_entry.get()}\n\nClick \'Ok\' to confirm.')

        if is_ok:
            with open(file_path, "a", newline='', encoding="cp437", errors='ignore') as pass_file:
                pass_file.write(
                    f'{website_entry.get()}\t\t{email_usn_entry.get()}\t\t{password_entry.get()}\n')

        # menghapus entry website dan password user ketika data sudah disimpan
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        # akan menaruh kursor di kolom website_entry
        website_entry.focus()


# membuat window dari aplikasi, mengubah judul aplikasi, mengatur padding x dan y
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# membuat canvas untuk menampilkan logo.png pada baris ke-0 kolom ke-1
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# membuat label website, email, dan password berderet ke bawah
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_usn_label = Label(text='Email/Username:')
email_usn_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# membuat entry website, email, dan password berderet ke bawah
# menginsert email user yang biasanya digunakan untuk suatu website
# columnspan untuk mengambil x kolom untuk lebarnya
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()  # auto focusing the cursor
email_usn_entry = Entry()
email_usn_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_usn_entry.insert(0, 'dummy@gmail.com')
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# membuat button generate password pada baris ke-3 kolom ke-2. fungsi generate password
# membuat button add pada baris ke-4 kolom ke-1, mengambil 2 kolom untuk lebarnya. fungsi save data
generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text='Add', command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# looping program
window.mainloop()