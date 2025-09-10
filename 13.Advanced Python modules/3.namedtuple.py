from collections import namedtuple
dog=namedtuple('dog',['age','breed','name'])
sammy=dog(age=10,breed='Husky',name='Sam')
print(sammy)
print(sammy.age)
print(sammy.name)
print(sammy.breed)