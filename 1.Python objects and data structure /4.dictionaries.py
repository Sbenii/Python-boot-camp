#Basic dictionary operations
Mydic={'Name':'Sezerano','Surname':'Beni'}
print(Mydic)
print(f"The name is: {Mydic['Name']} {Mydic['Surname']}")
prices={'Apple':2.99,'Mango':2.01,'Orange':3,'Pineapple':4.81,'Watermelon':5.01}
print(f"The price of one mango: {prices['Mango']}")
d={'K1':123,'K2':['a','b','c'],'k3':{'k4':[4,5,6]}}
print(f"{d['k3']['k4']}")

print(f"{d['K2'][2].upper()}")