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


