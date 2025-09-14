x=[1,2,3]
x.append([4,5])
print(x)

x=[1,2,3]
x.extend([4,5])
print(x)#-->the better way 

l=[1,2,3,4]
l.insert(1,"Inserted")
print(l)
l.remove("Inserted")
print(l)