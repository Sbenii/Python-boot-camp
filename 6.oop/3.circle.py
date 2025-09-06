class Circle():
    pi=3.14
    def __init__(self,radius):
        self.r=radius
        self.area=radius**2*Circle.pi
    def get_circumfrence(self):
        return self.r*self.pi*2
R=int(input("Please enter the radius of the circle: "))
my_circle=Circle(R)
print("Pi:{}".format(my_circle.pi))
print("Radius: {}".format(my_circle.r))
print("Circumfrence: {}".format(my_circle.get_circumfrence()))
print("The area of the circle: {}".format(my_circle.area))