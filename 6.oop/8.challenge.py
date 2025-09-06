class Line:
    def __init__(self,coor1=(0,0),coor2=(0,0)):
        self.corx1=coor1[0]
        self.cory1=coor1[1]
        self.corx2=coor2[0]
        self.cory2=coor2[1]
    def distance(self):
        return ((self.corx2-self.corx1)+(self.cory2-self.cory1))**0.5
    def slope(self):
        return ((self.cory2-self.cory1)/(self.corx2-self.corx1))
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())