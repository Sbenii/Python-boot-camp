#Classes and their attributes
class Dog():
    species='Mammals'
    def __init__(self,mybreed,name,spots):
        self.my_attribute=mybreed
        self.name_attribute=name
        self.spot_attribute=spots
#----->Methods
    def bark(self,number):
        print("Woof!! my name is {} and the number is: {}".format(self.name_attribute,number))
my_dog=Dog(mybreed='German shepherd',name='Cy',spots=False)
print("A dog is in class of: "+my_dog.species)
print("My dog is: a "+my_dog.my_attribute)
print("My dog's name: "+my_dog.name_attribute)
print("Does my dog has spots?:",my_dog.spot_attribute)
my_dog.bark(10)
