class rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        a=self.length*self.breath
        return a
    def perimeter(self):
        b=2*(self.length+self.breath)
        return b
a=int(input("enter the length of first rectangle"))
b=int(input("enter the breath of first rectangle"))
c=int(input("enter the length of second rectangle"))
d=int(input("enter the breath of second rectangle"))
obj_1=rectangle(a,b)
obj_2=rectangle(c,d)
print("area of rectangle:",obj_1.area())
print("perimeter of a rectangle",obj_1.perimeter())
print("area of rectangle:",obj_2.area())
print("perimeter of rectangle",obj_2.perimeter())

if(obj_1.area()==obj_2.area()):
    print("both have same area",obj_1.area)
elif obj_1.area()>obj_2.area():
    print("the first rectangle is greater",obj_1.area())
else:
    print("the second rectangle is grearter",obj_2.area())
