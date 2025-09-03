#Returning 5% of the sum
def myfunc(*args):
    return sum(args)*0.05
sum=myfunc(1,2,545,23,12,67,88,2)
print(f"The sum of the given numbers: {sum}")