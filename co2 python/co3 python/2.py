from graphics.circle import *
import graphics.rect
import graphics.sphere
from graphics import cuboid
l=int(input("enter length"))
b=int(input("enter breadth"))
h=int(input("enter height"))
r=int(input("enter radius"))
print("area of rectangle:"+str(graphics.rect.getperimeter(l,b)))
print("area of sphere:"+str(graphics.sphere.getarea(l)))
print("area of cuboid:"+str(cuboid.getarea(l,b,h)))
print("area of circle:"+str(area(r)))
 
