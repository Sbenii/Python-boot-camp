x=50
def num():
    global x
    print(f'x: {x}')
    x='New value'
    print(F"X was updated to a global: {x}")   
print(x)
num()
print(x)
    