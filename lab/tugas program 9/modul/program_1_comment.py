# mengimport module ABC dan abstractmethod dari library abc
from abc import ABC, abstractmethod

# membuat class bernama Animal menggunakan ABC
class Animal(ABC):
    # kelas abstrak untuk menentukan interface umum
    @abstractmethod
    # method untuk inisialsasi
    def __init__(self, name):
        self.name = name
    # method untuk menaruh info
    def info(self):
        print(f"I am an animal. My name is {self.name}")
    # method sound
    def sound():
        pass

# membuat subclass Animal dengan nama Cat
class Cat(Animal):
    # method untuk inisialisasi
    def __init__(self, name):
        super().__init__(name)
    # method untuk menaruh info
    def info(self):
        print(f"I am a cat. My name is {self.name}")
    # method suara Cat
    def sound(self):
        print("Meow")

# membuat subclass Animal dengan nama Dog
class Dog(Animal):
    # method untuk inisialisasi
    def __init__(self, name):
        super().__init__(name)
    # method untuk menaruh info
    def info(self):
        print(f"I am a dog. My name is {self.name}")
    # method untuk suara Dog
    def sound(self):
        print("Woof")

# membuat instance dari Cat dengan nama Win
A = Cat("Win")
# membuat instance dari Dog dengan nama Wan
B = Dog("Wan")
# menampilkan suara Cat Win
A.sound()
# menampilkan suara Dog Wan
B.sound()