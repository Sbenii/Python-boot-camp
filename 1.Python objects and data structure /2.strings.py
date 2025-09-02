print("Hello\nWorld!!" ) #Printing world on the next line
print("Hello \t World!!") #Printing world with a tab space
print(len("Hello world")) #Printing the lenght of the string
mystring="Hello world"
#Grabbing a single character
print(mystring[4])
print(mystring[8])
#Grabbing a single character by reverse method
print(mystring[-1])
print(mystring[-2])
#Slicing
mystring="abcdefghijk"
print(mystring[2:])#left to right
print(mystring[:4])#right to left
print(mystring[3:7])#in-between
#Step size
print(mystring[::2])
print(mystring[::3])
print(mystring[2::2])
print(mystring[1:7:2])
#Reversing the string
print(mystring[::-1])
#Editing the string
newstring=mystring[8:]+"lmnopqrst"
print(newstring)
#String multiplication
newstring='b'*10
print(newstring)
#String methods
x='Hello world'
print(x.upper())
print(x.split())
x='Hi this is a string'
print(x.split('i'))
#Formatting using .format() method
print("{} {}".format("Welcome","back!!!"))
print("This is a {1} {2} {0}".format('fox', 'quick', 'brown'))
print('{a} {b} {c} {d} {e}'.format(a='My', b='name', c='is', d='Sezerano', e='Beni!!🏀'))
result=0.121723434968
print("The result is: {}".format(result))
print("The result rounded off is: {r:.3f}".format(r=result))
#Formatting using f string
name='Beni🧩'
print(f"Hello my name is {name}")
age=20;
print(f"{name} is {age} years old.")


