class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('talk')

    def say_hi(self):
        print(f'Hi, my name is {self.name}.')

person1 = Person('Nasywa')
person1.talk()
person1.say_hi()