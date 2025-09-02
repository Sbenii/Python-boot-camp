#List basic operations
Mylist=[1,2,3,4,5]
Mylist1=['Hello',1000,20.5]
print(len(Mylist))
print(len(Mylist1))
print(Mylist[2])
print(Mylist1[1:])
print(Mylist1[:1])
Mylist2=[6,7,8,9,10]
newlist=Mylist+Mylist2
print(newlist)
Mylist1[1]='Sir'
print(Mylist1)
newlist.append(11)#adding an element to the list
print(newlist)
print(newlist.pop())#removing the last element
print(newlist)
print(Mylist.pop(4))
print(Mylist)
#Sorting a list
Newlist=['a','f','v','c','d','z']
Numlist=[3,2,6,1,8,0]
print(f"Unsorted list: {Newlist}")
print(f"Unsorted numbers: {Numlist}")
Newlist.sort()
Numlist.sort()
print(f"Sorted list: {Newlist}")
print(f"Sorted number: {Numlist}")
#Reversing a string
Newlist.reverse()
Numlist.reverse()
print(f"Reversed list: {Newlist}")
print(f"Reversed numbers: {Numlist}")

