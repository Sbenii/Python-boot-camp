#For loop operators
#Appending a list using for loop
mystring='Hello'
mylist=[]
for i in mystring:
    mylist.append(i)
print(mylist)    
#Alternative and easy way
mylist=[x for x in "Beni"]
print(mylist)
otherlist=[x for x in "Lists"]
print("The other list: ",otherlist)
#Iterations operator
num=[x for x in range(0,11)]
print(num)
num=[x**2 for x in range(0,11)]
print(num)
#Adding the if statement
num=[x for x in range(0,11) if (x%2==0)]
print(num)
#Using formulas
celcius=[0,10,20,34.5,100]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(f"Temperature in celcius: {celcius}")
print(f"Temperature in fahrenheit: {fahrenheit}")
