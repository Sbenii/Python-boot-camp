class Animal():
    def __init__(self,name):
        self.n=name
    def speak(self):
        raise NotImplementedError ("Subclass must implement this abstract method!!!")
class Dog(Animal):
    def speak(self):
        print(self.n+" says woof!!")
class Cat(Animal):
    def speak(self):
        print(self.n+" says meow!!")
max=Dog('Max')
ket=Cat('Ket')
max.speak()
ket.speak()