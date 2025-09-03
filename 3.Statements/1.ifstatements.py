a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))
d=(b*b)-(4*a*c)
print(f"Delta of the equation: {d}")
if (d>0):
    root1=(-(b)+(d**0.5))/(2*a)
    root2=(-(b)-(d**0.5))/(2*a)
    print("We have two distinct roots!!!")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif (d==0):
    root1=(-(b)+(d**0.5))/(2*a)
    root2=root1
    print("We have two double roots!!!")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
else:
    print("We have no real roots!!!")
