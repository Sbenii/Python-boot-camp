#Lambda expression, map and filter expressions
def square(num):
    return num**2
my_nums=[1,2,3,4,5,6]
for i in map(square,my_nums):
    print(i)