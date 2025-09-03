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
print(otherlist)
