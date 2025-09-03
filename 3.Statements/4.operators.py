#for operators
for i in range(10):
    print(i)
print('\n')
for i in range (2,10):
    print (i)
print('\n')
for i in range (0,11,2):
    print (i)
print('\n')
#Enumerate function
word='Sezerano'
for i in enumerate(word):
    print(i)
print('\n')
#Zip function
li1=[1,2,3]
li2=['a','b','c']
li3=[4,5,6]
for i in zip(li1,li3,li2):
    print(i)
#Simple search
print('x' in li2)
#min and max
num=[10,20,30,40,50,70]
print("The minimum number in the list: ",min(num))
print("The maximum number in the list: ",max(num))
#shuffle library
from random import shuffle as sh
mylist=[1,2,3,4,5,6,7,8,9,10]
sh(mylist)
print("Shuffled list: ",mylist)
#randint library~this gives a random integer in a given range
from random import randint as ran
print(ran(0,1983764))