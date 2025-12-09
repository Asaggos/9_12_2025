# #Askhsh 1

# class UpperString():

#     def getString(self , a):
#         self.word = a

#     def printString(self):
#         print(str.upper(self.word))

# leksh = UpperString()
# leksh.getString(input("Dwse leksh me mikra na to kanw megala: "))
# leksh.printString() 


# #Askhsh 2

# class Rectangle():
    
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def CalcArea(self):
#         return self.length * self.width
    
# Orthogonio = Rectangle(3,3)
# print("Emvadon: " ,Orthogonio.CalcArea())

#Askhsh 3

# p = 3.14159

# class Circle():
    
#     def __init__(self,radius):
#         self.radius = radius

#     def Emvado(self):
#         return p * (self.radius**2)
    
#     def perimetros(self):
#         return 2 * p * self.radius
    
# c = Circle(5)

# print ("Emvado= ", c.Emvado())
# print ("Perimetros= " , c.perimetros())



# #Askhsh 4

# import math

# class Vector():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def ReadData(self):
#         x= int(input("X: "))
#         y= int(input("Y: "))

#         return x, y

#     def SetData(self,xi,yi):
#         self.x=xi
#         self.y=yi

#     def PrintData(self):
#         print("X = " , self.x ,"\nY = ", self.y)

#     def metro(self):
#         return   math.sqrt(self.x**2 + self.y**2)


# v1 = Vector(1,2)
# v1.PrintData()

# v2 = Vector(0,0)
# x , y = v2.ReadData()
# v2.SetData(x,y)
# v2.PrintData()

# metro1 = v1.metro()
# metro2 = v2.metro()

# print(f"Metro1: {metro1:.2f} \nMetro2: {metro2:.2f}")