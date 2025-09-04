#Returning 5% of the sum
#args deals with tuples
def myfunc(*args):
    return sum(args)*0.05
sum=myfunc(1,2,545,23,12,67,88,2)
print(f"The sum of the given numbers: {sum}")
#kwargs deals with dictionaries
def myfunc2(**kwargs):
    print (kwargs)
    if 'fruit' in kwargs:
        print ('My choice of fruit: {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here!!!')
myfunc2(fruit='Apple', veggie='Carbagge')
#Combination of the two
def myfunc3(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[1],kwargs["Food"]))
myfunc3(10,20,30,40,Food='Eggs',drink='water',fruit='apple')

def myfunc4(*k):
    mylist=[]
    for i in k:
        if i%2==0:
            mylist.append (i)
    return mylist
myfunc4(1,2,3,4,5,6)

