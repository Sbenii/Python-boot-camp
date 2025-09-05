class Dog():
    def __init__(self,name):
        self.n=name
    def speak(self):
        return self.n+" says woofwoof!!"
class Cat():
    def __init__(self,name):
        self.n=name
    def speak(self):
        return self.n + " says meowmeow!!"
nike=Dog('Niko')
Bund=Cat('Benji')
my_animal=Dog(nike)
print(nike.speak())
print(Bund.speak())