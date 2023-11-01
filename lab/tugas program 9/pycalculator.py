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
    
angka_1 = input('Masukkan angka pertama : ')
angka_2 = input('Masukkan angka kedua : ')