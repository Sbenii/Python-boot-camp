#Returning 5% of the sum
#args
def myfunc(*args):
    return sum(args)*0.05
sum=myfunc(1,2,545,23,12,67,88,2)
print(f"The sum of the given numbers: {sum}")
#kwargs
def myfunc2(**kwargs):
    print (kwargs)
    if 'fruit' in kwargs:
        print ('My choice of fruit: {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here!!!')
myfunc2(fruit='Apple',veggie='Carbagge')