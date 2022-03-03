print("area of square")
area_of_sqr=lambda x:x*x
side=int(input("the value of side"))
print("area of square is ",area_of_sqr(side))

print("area of rectangle")
area_of_rect=lambda a,b:a*b
a=int(input("enter the length"))
b=int(input("enter the breath"))
print("area of rectangle is",area_of_rect(a,b))

print("area of triangle")
area_of_tri=lambda b,h:0.5*b*h
b=int(input("enter the breath"))
h=int(input("enter the height"))
print("area of triangle",area_of_tri(b,h))
