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
    
class Bagi(Calculator):
    def calculate(self):
        try:
            return self.first / self.second
        except ZeroDivisionError:
            print('\nTidak bisa membagi dengan angka nol.')

class Akar(Calculator):
    def calculate(self):
        return math.sqrt(self.first)

class Pangkat(Calculator):
    def calculate(self):
        return self.first**self.second
    
def re_run():
    global program
    choice = input('\nLanjutkan program? ("Ya" atau "Tidak)\nInput -> ').lower()
    if choice == 'tidak':
        program = False
    elif choice != 'ya':
        program = False
        print('\nInput Anda invalid.')

header = '''==============================================
||     + -      PYCALCULATOR       * /      ||
=============================================='''

program = True

while program:

    os.system('cls')
    print(header)
    list_operasi = ['Pertambahan', 'Pengurangan', 'Perkalian', 'Pembagian', 'Akar', 'Pangkat']

    pilihan_user = int(input('Silakan pilih operasi yang ingin Anda gunakan.\n1. Pertambahan\
                        \n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Akar\n6. Pangkat\
                             \n7. Keluar\nInput -> '))

    os.system('cls')
    print(header)

    if pilihan_user in range(1, 5):

        print(list_operasi[pilihan_user-1])
        angka_1 = int(input('Masukkan angka pertama\t: '))
        angka_2 = int(input('Masukkan angka kedua\t: '))

        if pilihan_user == 1:
            sum_result = Tambah(angka_1, angka_2)
            print(f'\nHasil penjumlahan dari {angka_1} + {angka_2} adalah {sum_result.calculate()}.')
            re_run()
        elif pilihan_user == 2:
            sub_result = Kurang(angka_1, angka_2)
            print(f'\nHasil pengurangan dari {angka_1} - {angka_2} adalah {sub_result.calculate()}.')
            re_run()
        elif pilihan_user == 3:
            mul_result = Kali(angka_1, angka_2)
            print(f'\nHasil perkalian dari {angka_1} * {angka_2} adalah {mul_result.calculate()}.')
            re_run()
        elif pilihan_user == 4:
            div_result = Bagi(angka_1, angka_2)
            print(f'\nHasil pembagian dari {angka_1} / {angka_2} adalah {div_result.calculate()}.')
            re_run()
    
    elif pilihan_user == 5:
        print(list_operasi[pilihan_user-1])
        angka_1 = int(input('Masukkan angka\t: '))
        root_result = Akar(angka_1, None)
        print(f'\nHasil akar dari {angka_1} adalah {root_result.calculate()}.')
        re_run()
    elif pilihan_user == 6:
        print(list_operasi[pilihan_user-1])
        angka_1 = int(input('Masukkan angka\t: '))
        angka_2 = int(input('Masukkan pangkat: '))
        root_result = Pangkat(angka_1, angka_2)
        print(f'\nHasil pangkat {angka_2} dari {angka_1} adalah {root_result.calculate()}.')
        re_run()
    elif pilihan_user == 7:
        program = False
    else :
        print('\nInput Anda invalid.')
        program = False

print('\nProgram telah dihentikan.')
print('==============================================')
