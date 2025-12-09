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

p = 3.14159

class Circle():
    
    def __init__(self,radius):
        self.radius = radius

    def Emvado(self):
        return p * (self.radius**2)
    
    def perimetros(self):
        return 2 * p * self.radius
    
c = Circle(5)

print ("Emvado= ", c.Emvado())
print ("Perimetros= " , c.perimetros())
