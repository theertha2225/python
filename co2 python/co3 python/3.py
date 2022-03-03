class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        return a
    def perimeter(self):
        b=2*(self.length+self.breadth)
        return b
a=int(input("enter the length of first rectangle"))
b=int(input("enter breadth of first rectangle"))
c=int(input("enter the length of second rectangle"))
d=int(input("enter the breadth of second rectangle"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
print("area of rec",obj1.area(),"and","perimeter of rec",obj1.perimeter())
print("area of rec",obj2.area(),"and","perimeter of rec",obj2.perimeter())
if(obj1.area()==obj2.area()):
    print("both rectangle have same area",obj1.area())
elif obj1.area()>obj2.area():
   print("first rectangle is greater",obj1.area())
else:
   print("second rectangle is greater",obj2.area())
