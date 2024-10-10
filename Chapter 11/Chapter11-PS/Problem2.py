class Animal:
    pass

class Pets:
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bark,Bark")

d = Dog()
d.bark()