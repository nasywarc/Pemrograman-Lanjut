# Nasywa Azizah Zharifah
# 225150307111060

class Calculator:
    def __init__(self, first_number, second_number):
        self.a = first_number
        self.b = second_number

    def calculate(self):
        pass

class Tambah(Calculator):
    def calculate(self):
        return self.a + self.b
    
class Kurang(Calculator):
    def calculate(self):
        return self.a - self.b
    
class Kali(Calculator):
    def calculate(self):
        return self.a * self.b
    
class Bagi(Calculator):
    def calculate(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print('Tidak bisa membagi dengan angka nol.\n')
    
angka_1 = int(input('Masukkan angka pertama : '))
angka_2 = int(input('Masukkan angka kedua : '))

sum_result = Tambah(angka_1, angka_2)
sub_result = Kurang(angka_1, angka_2)
mul_result = Kali(angka_1, angka_2)
div_result = Bagi(angka_1, angka_2)

print(f'\nHasil penjumlahan dari {angka_1} + {angka_2} adalah {sum_result.calculate()}')
print(f'Hasil pengurangan dari {angka_1} - {angka_2} adalah {sub_result.calculate()}')
print(f'Hasil perkalian dari {angka_1} * {angka_2} adalah {mul_result.calculate()}')
print(f'Hasil pembagian dari {angka_1} / {angka_2} adalah {div_result.calculate()}')
