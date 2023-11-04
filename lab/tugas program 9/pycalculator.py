# PYCALCULATOR PROGRAM
# Nasywa Azizah Zharifah
# 225150307111060

# mengimport module os untuk membersihkan terminal
import os
# mengimport module math untuk menghitung akar
import math

# membuat class bernama Calculator
class Calculator:
    # method __init__ untuk menginisialisasi object
    def __init__(self, first_number, second_number):
        self.first = first_number
        self.second = second_number

    # method calculate pada class Calculator
    def calculate(self):
        pass

# membuat subclass Tambah dari class Calculator
class Tambah(Calculator):
    # menggunakan polimorfisme untuk meng-overide method calculate
    def calculate(self):
        return self.first + self.second
    
# membuat subclass Kurang dari class Calculator
class Kurang(Calculator):
    # menggunakan polimorfisme untuk meng-overide method calculate
    def calculate(self):
        return self.first - self.second
    
# membuat subclass Kali dari class Calculator
class Kali(Calculator):
    # menggunakan polimorfisme untuk meng-overide method calculate
    def calculate(self):
        return self.first * self.second
    
# membuat subclass Bagi dari class Calculator
class Bagi(Calculator):
    # menggunakan polimorfisme untuk meng-overide method calculate
    def calculate(self):
        # menggunakan perintah try untuk mengantisipasi error
        try:
            return self.first / self.second
        # jika terjadi ZeroDivisionError, maka akan menampilkan pesan
        except ZeroDivisionError:
            print('\nTidak bisa membagi dengan angka nol.')

# membuat subclass Akar dari class Calculator
class Akar(Calculator):
    # menggunakan polimorfisme untuk meng-overide method calculate
    def calculate(self):
        return math.sqrt(self.first)

# membuat subclass Pangkat dari class Calculator
class Pangkat(Calculator):
    # menggunakan polimorfisme untuk meng-overide method calculate
    def calculate(self):
        return self.first**self.second

# membuat fungsi untuk memberi pilihan ke user lanjut atau tidak    
def re_run():
    global program
    choice = input('\nLanjutkan program? ("Ya" atau "Tidak)\nInput -> ').lower()
    if choice == 'tidak':
        program = False
        print('\nProgram telah dihentikan.')
        print('==============================================')
    elif choice != 'ya':
        program = False
        print('\nInput Anda invalid.')

# membuat fungsi untuk menampilkan pilihan_user
def print_operasi():
    print('')
    print(list_operasi[pilihan_user-1])

# membuat string variabel header
header = '''==============================================
||     + -      PYCALCULATOR       * /      ||
=============================================='''

# membuat variable bool program bernilai True
program = True

# loop program
while program:

    os.system('cls')
    print(header)
    # membuat list untuk operasi
    list_operasi = ['Pertambahan', 'Pengurangan', 'Perkalian', 'Pembagian', 'Akar', 'Pangkat']
    
    # prompt ke user
    pilihan_user = int(input('Silakan pilih operasi yang ingin Anda gunakan.\n1. Pertambahan\
                        \n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Akar\n6. Pangkat\
                             \n7. Keluar\nInput -> '))
    
    # jika pilihan_user dalam range 1-5
    if pilihan_user in range(1, 5):
        
        # menampilkan operasi pilihan_user
        print_operasi()
        is_int = False
        # membuat looping selama input user bukan int
        # menangkap error ValueError
        while not is_int:
            try:
                angka_1 = int(input('Masukkan angka pertama\t: '))
                is_int = True
            except ValueError:
                print('Hanya bisa menerima input angka.\n')

        is_int = False
        while not is_int:
            try:
                angka_2 = int(input('Masukkan angka kedua\t: '))
                is_int = True
            except ValueError:
                print('Hanya bisa menerima input angka.\n')

        
        # jika pilihan_user adalah 1 (pertambahan)
        if pilihan_user == 1:
            sum_result = Tambah(angka_1, angka_2)
            print(f'\nHasil penjumlahan dari {angka_1} + {angka_2} adalah {sum_result.calculate()}.')
            re_run()
        # jika pilihan_user adalah 2 (pengurangan)
        elif pilihan_user == 2:
            sub_result = Kurang(angka_1, angka_2)
            print(f'\nHasil pengurangan dari {angka_1} - {angka_2} adalah {sub_result.calculate()}.')
            re_run()
        # jika pilihan_user adalah 3 (perkalian)
        elif pilihan_user == 3:
            mul_result = Kali(angka_1, angka_2)
            print(f'\nHasil perkalian dari {angka_1} * {angka_2} adalah {mul_result.calculate()}.')
            re_run()
        # jika pilihan_user adalah 4 (pembagian)
        elif pilihan_user == 4:
            div_result = Bagi(angka_1, angka_2)
            print(f'\nHasil pembagian dari {angka_1} / {angka_2} adalah {div_result.calculate()}.')
            re_run()
    
    # jika pilihan_user adalah 5 (pengakaran)
    elif pilihan_user == 5:
        print_operasi()
        is_int = False
        # membuat looping selama input user bukan int
        # menangkap error ValueError
        while not is_int:
            try:
                angka_1 = int(input('Masukkan angka\t: '))
                is_int = True
            except ValueError:
                print('Hanya bisa menerima input angka.\n')
        root_result = Akar(angka_1, None)
        print(f'\nHasil akar dari {angka_1} adalah {root_result.calculate()}.')
        re_run()
    # jika pilihan_user adalah 6 (pemangkatan)
    elif pilihan_user == 6:
        print_operasi()
        is_int = False
        # membuat looping selama input user bukan int
        # menangkap error ValueError
        while not is_int:
            try:
                angka_1 = int(input('Masukkan angka\t: '))
                is_int = True
            except ValueError:
                print('Hanya bisa menerima input angka.\n')
        is_int = False
        while not is_int:
            try:
                angka_2 = int(input('Masukkan pangkat: '))
                is_int = True
            except ValueError:
                print('Hanya bisa menerima input angka.\n')

        root_result = Pangkat(angka_1, angka_2)
        print(f'\nHasil pangkat {angka_2} dari {angka_1} adalah {root_result.calculate()}.')
        re_run()
    # jika pilihan_user adalah 7 (keluar program)
    elif pilihan_user == 7:
        program = False
        print('\nProgram telah dihentikan.')
        print('==============================================')
    else :
        program = False
        print('\nInput Anda invalid.')

