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
li2=[(1,2,3),(4,5,6),(7,8,9)]
for (a,b,c) in li2:
    print(c)
#Dctionaries
d={'k1':1,'k2':2,'k3':3}
for i in d:
    print(i)#this will print only keys
for i in d.values():
    print (i)#this will print only values
for i in d.items():
    print(i)#this will print keys with their values
for (a,b) in d.items():
    print(b)#selecting what to print btn keys and values
#pass, continue and break keywords
x=[1,2,3]
for i in x:
    pass
print("End of the script!!")

x='Sammy'
for i in x:
    if i=='y' or i=='S':
        continue
    print(i)

x="Benioeoeo"
for i in x:
    if i=='o':
        break
    print(i)