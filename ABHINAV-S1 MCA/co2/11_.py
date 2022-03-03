square=lambda x:x*x
side=int(input("enter length of aside of square"))
print("area of square is",square(side))

rectangle=lambda a,b:a*b
a=int(input("enter the length of rectange"))
b=int(input("enter the bredth of rectangle"))
print("area of rectangle",rectangle(a,b))

triangle=lambda b,h:0.5*b*h
b=int(input("enter the bredth of triangle"))
h=int(input("enter the  height of the triangle"))
print("area of triangle",triangle(b,h))
