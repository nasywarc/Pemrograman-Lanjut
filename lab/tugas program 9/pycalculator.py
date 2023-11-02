# Nasywa Azizah Zharifah
# 225150307111060

import os
import math

class Calculator:
    def __init__(self, first_number, second_number):
        self.first = first_number
        self.second = second_number

    def calculate(self):
        pass

class Tambah(Calculator):
    def calculate(self):
        return self.first + self.second
    
class Kurang(Calculator):
    def calculate(self):
        return self.first - self.second
    
class Kali(Calculator):
    def calculate(self):
        return self.first * self.second
    
class Bagi(Calculator):
    def calculate(self):
        try:
            return self.first / self.second
        except ZeroDivisionError:
            print('Tidak bisa membagi dengan angka nol.')

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
    list_operasi = ['Pertambahan', 'Pengurangan', 'Perkalian', 'Pembagian']

    pilihan_user = int(input('Silakan pilih operasi yang ingin Anda gunakan.\n1. Pertambahan\
                        \n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Keluar\nInput -> '))

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
        program = False
    else :
        print('\nInput Anda invalid.')

print('\nProgram telah dihentikan.')
print('==============================================')
