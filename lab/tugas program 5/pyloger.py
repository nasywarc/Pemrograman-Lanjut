# PROGRAM PYLOGER (Python Login & Register)
# Nasywa Azizah Zharifah
# 225150307111060

# mengimport module os dan csv untuk digunakan
import os
import csv

# menyapa user dan memberikan pilihan pada user antara login dan register
print("===============================================")
print("Welcome to Pyloger.\n")
print('1. Register\n2. Login')
user__choice = input("\nType your choice : ")

# kondisi jika user memilih register
if user__choice == '1':

    # menyimpan nama dan pass serta access user
    print("You're going to create a new account.\n")
    new_user__name = input("Enter your name : ")
    new_user__pass = input("Enter your password : ")
    new_user__access = input("Are you an admin? ")

    # kondisi jika input == iamgod
    if new_user__access == 'iamgod':  # untuk admin

        # kondisi jika sudah terdapat file users.csv, akan menggunakan a (append)
        # setelah itu mengisi sesuai input user
        if os.path.exists("./users.csv"):
            with open("./users.csv", "a", newline='') as users__data:
                field_names = ['name', 'pass', 'access']
                writer = csv.DictWriter(users__data, fieldnames=field_names)
                writer.writerow(
                    {'name': new_user__name, 'pass': new_user__pass, 'access': '1'})
                print("\nYour account has been created.")
                print("===============================================")

        # jika file belum terbuat, akan menggunakan x (create)
        # setelah itu membuat atribut name, pass, dan access user dan mengisi sesuai-
        # input user
        else:
            with open("./users.csv", "x", newline='') as users__data:
                field_names = ['name', 'pass', 'access']
                writer = csv.DictWriter(users__data, fieldnames=field_names)
                writer.writeheader()  # menuliskan header yaitu name, pass, access
                writer.writerow(
                    {'name': new_user__name, 'pass': new_user__pass, 'access': '1'})
                print("\nYour account has been created.")
                print("===============================================")

    # kondisi jika input != iamgod
    else:  # untuk guest

        # kondisi jika sudah terdapat file users.csv, akan menggunakan a (append)
        # setelah itu mengisi sesuai input user
        if os.path.exists("./users.csv"):
            with open("./users.csv", "a", newline='') as users__data:
                field_names = ['name', 'pass', 'access']
                writer = csv.DictWriter(users__data, fieldnames=field_names)
                writer.writerow(
                    {'name': new_user__name, 'pass': new_user__pass, 'access': '0'})
                print("\nYour account has been created.")
                print("===============================================")

        # jika file belum terbuat, akan menggunakan x (create)
        # setelah itu membuat atribut name, pass, dan access user dan mengisi sesuai-
        # input user
        else:
            with open("./users.csv", "x", newline='') as users__data:
                field_names = ['name', 'pass', 'access']
                writer = csv.DictWriter(users__data, fieldnames=field_names)
                writer.writeheader()  # menuliskan header yaitu name, pass, access
                writer.writerow(
                    {'name': new_user__name, 'pass': new_user__pass, 'access': '0'})
                print("\nYour account has been created.")
                print("===============================================")

# kondisi jika user memilih login
elif user__choice == '2':

    # kondisi jika sudah terdapat file users.csv
    # program akan menanyakan name dan pass user
    if os.path.exists("./users.csv"):
        print("You will be directed to log in.\n")
        user__name = input('Enter your name : ')
        user__pass = input('Enter your password : ')

        # membuka file users.csv untuk dibaca (read)
        with open("./users.csv", "r", newline='') as users__data:
            field_names = ['name', 'pass', 'access']
            reader = csv.DictReader(users__data)
            found = False

            # melakukan perulangan sampai menemukan baris yang sesuai dg input user
            # jika ada, index access dan nama akan disimpan
            # access_index untuk menentukan hak akses
            # log_in_username untuk menampilkan nama user
            for row in reader:
                if row['name'] == user__name and row['pass'] == user__pass:
                    access_index = (row['access'])
                    log_in_username = (row['name'])
                    found = True

            # jika akun ditemukan, var found akan berubah jadi true
            # membuat kondisi jika found bernilai true
            if found:

                # membuat kondisi jika user memiliki access sebagai admin
                # program akan membuka file hello.txt untuk ditulis-
                # kalimat sambutan untuk admin
                # setelah itu program akan membuka file untuk dibaca lalu ditampilkan
                if access_index == '1':
                    with open("./hello.txt", "w") as greeting_admin:
                        greeting_admin.write("LOGIN STATUS : SUCCESS.")
                        greeting_admin.write(f"\nWelcome, {log_in_username}.")
                        greeting_admin.write(
                            "\nYou have successfully logged in as a \"Admin\".")
                    with open("./hello.txt", "r") as greeting_admin:
                        print("\n" + greeting_admin.read())
                        print("===============================================")

                # membuat kondisi jika user memiliki access sebagai guest
                # program akan membuka file hello.txt untuk ditulis-
                # kalimat sambutan untuk guest
                # setelah itu program akan membuka file untuk dibaca lalu ditampilkan
                else:
                    with open("./hello.txt", "w") as greeting_guest:
                        greeting_guest.write("LOGIN STATUS : SUCCESS.")
                        greeting_guest.write(f"\nWelcome, {log_in_username}.")
                        greeting_guest.write(
                            "\nYou have successfully logged in as a \"Guest\".")
                    with open("./hello.txt", "r") as greeting_guest:
                        print("\n" + greeting_guest.read())
                        print("===============================================")

            # jika akun tidak ditemukan, maka program akan membuka file hello.txt-
            # untuk ditulis kalimat lain yang memberitahu bahwa nama/pass salah
            # setelah itu program akan membuka file untuk dibaca lalu ditampilkan
            else:
                with open("./hello.txt", "w") as failed:
                    failed.write("LOGIN STATUS : FAILED.")
                    failed.write(
                        "\nPlease check your correct name or password.")
                with open("./hello.txt", "r") as failed:
                    print("\n" + failed.read())
                    print("===============================================")

    # kondisi jika belum terdapat file users.csv (belum terdapat akun)
    else:
        print("\nThere is no such account.")
        print("===============================================")

# kondisi jika input yang dimasukkan user tidak sesuai pilihan
else:
    print('\nYour input is invalid.')
    print("===============================================")
