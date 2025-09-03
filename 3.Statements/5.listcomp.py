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
results=[x if x%2==0 else "Odd!!" for x in range (0,7)]
print(results)
#Using formulas
celcius=[0,10,20,34.5,100]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(f"Temperature in celcius: {celcius}")
print(f"Temperature in fahrenheit: {fahrenheit}")
#or you can use this way:
cel=[0,10,20,30,40,50]
fah=[]
for i in cel:
    fah.append((9/5)*i+32)
print(f"Temperature in celcius: {cel}")
print(f"Temperature in fahrenheit: {fah}")
#nested loops
nest=[]
for x in [2,4,6]:
    for y in [1,10,100]:
        nest.append(x*y)
print(f"Nested loop: {nest}")
#Alternative
nest=[x*y for x in [2,4,6] for y in [1,10,100]]
print(f"Nested loop: {nest}")