import random
#random.seed(20)#-->Helps retaining a given random number on its unique sequence!!!
randomnbr=random.randint(0,100)
print(randomnbr)
print(randomnbr)
mylist=list(range(0,30))
print(mylist)
print(random.choice(mylist))
#Sample with replacement
print(random.choices(population=mylist,k=10))
#Sample without replacement
print(random.sample(population=mylist,k=10))
random.shuffle(mylist)
print(mylist)
print(random.uniform(0,10))

