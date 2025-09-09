from collections import Counter
my_list=[1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4]
print(Counter(my_list))
my_list=['a','a','a',1,1,1,1,'b','b']
print(Counter(my_list))
mylist=('aaaaaaaaabbbbbannnnnaaaiiiiiaoooo')
print(Counter(mylist))
sentence='How many times does each word comes in this sentence?'
print(Counter(sentence.split()))
sentence2='Hello'