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
Niko=Dog('Niko')
Benji=Cat('Benji')
print(Niko.speak())
print(Benji.speak())
#-------------------------------
for pet in [Niko,Benji]:
    print(type(pet))
    print(pet.speak())
#-------------------------------
def pet_speak(pet):
    print(pet.speak())
pet_speak(Niko)