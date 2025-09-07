def add_num(n1,n2):
    return n1+n2
number1=20
number2=int(input("Enter the second number: "))
try:
   result=add_num(number1,number2)
except:
    print("An error occured while adding!!!")
else:
    print("Add went well")
    print("Sum: ",result)