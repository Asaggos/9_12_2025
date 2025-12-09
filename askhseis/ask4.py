#Askhsh 4

import math

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def ReadData(self):
        x= int(input("X: "))
        y= int(input("Y: "))

        return x, y

    def SetData(self,xi,yi):
        self.x=xi
        self.y=yi

    def PrintData(self):
        print("X = " , self.x ,"\nY = ", self.y)

    def metro(self):
        return   math.sqrt(self.x**2 + self.y**2)


v1 = Vector(1,2)
v1.PrintData()

v2 = Vector(0,0)
x , y = v2.ReadData()
v2.SetData(x,y)
v2.PrintData()

metro1 = v1.metro()
metro2 = v2.metro()

print(f"Metro1: {metro1:.2f} \nMetro2: {metro2:.2f}")