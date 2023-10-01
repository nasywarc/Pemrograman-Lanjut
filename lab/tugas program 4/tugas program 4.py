# PROGRAM PYCONVERSION
# Nasywa Azizah Zharifah
# 225150307111060

# mengimport modul tabulate untuk membuat tabel
from tabulate import tabulate

# membuat fungsi yang mengonversi bilangan integer ke bilangan biner
def int_to_bin (number) :
    binary = bin(number)
    return (binary)

# membuat fungsi yang mengonversi bilangan integer ke bilangan octal
def int_to_oct (number) :
    octal = oct(number)
    return (octal)

# membuat fungsi yang mengonversi bilangan integer ke bilangan hexadecimal
def int_to_hex (number) :
    hexa = hex(number)
    return (hexa)

# judul serta informasi untuk user
print("\nWelcome to Pyconversion.")
print("This program will help you convert integer numbers into binary, octal, or even hexadecimal.")
print("Hint : not just a converter.")

# membuat var bool yang digunakan untuk mengatur perulangan
loop = True

# membuat perulangan program agar tetap berulang
while loop :
    print("\nPlease choose one of the options you need.")
    # membuat pilihan/choice untuk user
    print("1. Integer to Binary\n2. Integer to Octal\n3. Integer to Hexadecimal\n4. Word Separator Game\n5. Make a List\nType \"exit\" to exit Pyconversion.")
    
    # menyimpan input user dalam var user__choice
    user__choice = input("\nType your input : ")

    # membuat kondisi dimana jika user mengetik "exit" maka loop akan berhenti
    if user__choice == 'exit' :
        loop = False

    # membuat kondisi dimana jika user mengetik "1" maka program akan mengonversi ke biner
    elif user__choice == '1' :
        user__input = int(input("Number you want to convert : "))
        binaryResult = int_to_bin(user__input) # memanggil fungsi int_to_bin untuk mengonversi input user ke biner
        print(f"\nThe result is {binaryResult}") # menampilkan hasil
        print("==============================================================")

    # membuat kondisi dimana jika user mengetik "2" maka program akan mengonversi ke octal
    elif user__choice == '2' :
        user__input = int(input("Number you want to convert : "))
        octalResult = int_to_oct(user__input) # memanggil fungsi int_to_oct untuk mengonversi input user ke octal
        print(f"\nThe result is {octalResult}") # menampilkan hasil
        print("==============================================================")

    # membuat kondisi dimana jika user mengetik "3" maka program akan mengonversi ke hexadecimal
    elif user__choice == '3' :
        user__input = int(input("Number you want to convert : "))
        hexaResult = int_to_hex(user__input) # memanggil fungsi int_to_hex untuk mengonversi input user ke hexadecimal
        print(f"\nThe result is {hexaResult}") # menampilkan hasil
        print("==============================================================")

    # membuat kondisi dimana jika user mengetik "4" maka program akan menjalankan sebuah permainan kata
    elif user__choice == '4' :
        your__word = input("Type your word here : ")
        your__start_range = int(input("Type your start range here : ")) # menyimpan range awal
        your__finish_range = int(input("Type your finish range here : ")) # menyimpan range akhir
        user_word_result = your__word[your__start_range:your__finish_range] # membuat hasil dari [range awal:range akhir] dari input user sendiri
        print(f"\nYour word result is \"{user_word_result}\"!") # menampilkan [range awal:range akhir] dari input user sendiri
        print("==============================================================")

    # membuat kondisi dimana jika user mengetik "5" maka program akan menjalankan sebuah list maker
    elif user__choice == '5' :
        list__title = input("What is the title of the list you want to create? ") # meminta user untuk membuat judul dari sebuah list
        your__list = [] # membuat list yang awalnya masih kosong
        loop_list = True # membuat bool untuk mengatur perulangan
        print("Please enter what you want to list. Type \"done\" if you're done.") # memberi informasi kepada user

        while loop_list :
            content = input("Add to your list -> ") # meminta input kepada user selama loop masih berjalan
            if content == 'done' : # membuat kondisi dimana loop berhenti saat user mengetikkan "done"
                break
            your__list.append(content) # menambahkan content ke dalam your__list

        header = ['', list__title] # mengatur header tabel
        list__total = range(1, len(your__list)+1) # membuat kolom nomor pada tabel
        table = zip(list__total, your__list) # menggabungkan list__total dan your__list agar menjadi satu tabel

        print("==============================================================")
        print(tabulate(table, header, tablefmt="plain")) # menampilkan tabel list pada user
        print("==============================================================")
        print(
        "Apakah \"Pemrograman Lanjut\" ada di list?",
        'Pemrograman Lanjut' in your__list
        )

    else :
        print("Your input is incorrect, please enter it again.") # kondisi jika input tidak sesuai
