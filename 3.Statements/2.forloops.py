#Basic operations
mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if (num%2==0):
        print(num)
    else: 
        print(f"Odd number!!!: {num}")    
sum=0
for num in mylist:
    sum=sum+num
print("sum:",sum)
#Tuples unpacking
li=[(1,2),(3,4),(5,6),(7,8)]
for i in li:
    print(i)
for (a,b) in li:
    print(a)
    print(b)
