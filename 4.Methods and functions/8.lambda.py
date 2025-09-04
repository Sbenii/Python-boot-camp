#Lambda expression, map and filter expressions
#list and map expressions
def square(num):
    return num**2
my_nums=[1,2,3,4,5,6]
for i in map(square,my_nums):
    print(i)
print(list(map(square,my_nums)))
#example 2
def splicer(mystr):
    if len(mystr)%2==0:
        return 'Even'
    else:
        return mystr[0]
namee=['Beni','Andyu','Gab']
print(list(map(splicer,namee)))
#Filter expression
def even(num):
    return num%2==0
my_nums=[1,2,3,4,5,6]
print(list(filter(even,my_nums)))
for i in filter(even,my_nums):
    print(i)
#Lambda expression
squares=lambda num:num**2
print(squares(3))