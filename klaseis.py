class Point:
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 8

p2.x = 5
p2.y = 8


p3 = p1
print(p3.x == p1.x)

p3.x = 15

class Rectagle:
    pass

box = Rectagle()

box.width = 10
box.height = 14


box.corner = Point()
box.corner.giorgos = 0
box.corner.y = 0


def growbox(antikeimeno, dwidth = 5, dheight = 6):
    box2 =Rectagle() 
    box2.height = antikeimeno.height + dheight
    box2.width = antikeimeno.width + dwidth
    return box2



tetragwno = growbox(box,4)
print("tetragwno.width",tetragwno.width)


import copy

p1 = Point()
p1.x = 3
p1.y = 4

p2 = copy.copy(p1)
print(p1.x == p2.x)
