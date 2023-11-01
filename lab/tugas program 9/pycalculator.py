# Nasywa Azizah Zharifah
# 225150307111060

class Calculator:
    def __init__(self, first_number, second_number):
        self.a = first_number
        self.b = second_number

    def calculate(self):
        pass

class Sum(Calculator):
    def calculate(self):
        return self.a + self.b
    
class Sub(Calculator):
    def calculate(self):
        return self.a - self.b
    
class Mul(Calculator):
    def calculate(self):
        return self.a * self.b
    
class Div(Calculator):
    def calculate(self):
        return self.a / self.b
    
angka_1 = int(input('Masukkan angka pertama : '))
angka_2 = int(input('Masukkan angka kedua : '))

sum_result = Sum(angka_1, angka_2)
sub_result = Sub(angka_1, angka_2)
mul_result = Mul(angka_1, angka_2)
div_result = Div(angka_1, angka_2)

print(f'Hasil penjumlahan dari {angka_1} + {angka_2} adalah {sum_result.calculate()}')