square=lambda x:x*x
side=int(input("enter side length of square "))
print("area of square is",square(side))

rect=lambda a,b:a*b
a=int(input("enter the length of rectangle"))
b=int(input("enter the breadth of rectangle"))
print("area of rectangle is",rect(a,b))

tri=lambda c,h:0.5*c*h
c=int(input("enter the base length of the triangle"))
h=int(input("enter the hieght of the triangle"))
print("area of triangle is",tri(c,h))
