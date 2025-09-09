def create_cubes(n):
    for i in range (n):
        yield (i**3)#----> We use yield as our generator!!
for x in create_cubes(10):
    print (x)
print(list(create_cubes(10)))
#-------------------------------------------------
def fibon(n):
    a=1
    b=1
    for x in range(n):
        yield a
        a,b=b,a+b
for number in fibon(10):
    print(number)
#--------------------------------------------------
def simple_gen():
    for x in range(3):
        yield x
for i in simple_gen():
    print (i)
    
g=simple_gen()
print(next(g))
print(next(g))
#---------------------------------------------------
word='Hello'
for x in word:
    print(x)
word_iter=iter(word)
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))
print(next(word_iter))

