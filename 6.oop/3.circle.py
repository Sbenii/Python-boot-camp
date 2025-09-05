class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.r=radius
        self.area=radius**2*Circle.pi
    def get_circumfrence(self):
        return self.r*self.pi*2
my_circle=Circle(30)
print("Pi:{}".format(my_circle.pi))
print("Radius: {}".format(my_circle.r))
print("Circumfrence: {}".format(my_circle.get_circumfrence()))
print("The area of the circle: {}".format(my_circle.area))