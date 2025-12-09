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
