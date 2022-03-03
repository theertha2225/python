class rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
    def perimeter(self):
        return 2*(self.breadth+self.length)
a=int(input("enter length of rectangle:"))
b=int(input("enter breadth of rectangle:"))
c=int(input("enter length of second rectangle:"))
d=int(input("enter breadth of second rectangle:"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
print("area of rectangle:",obj1.area(),"and","perimeter of rec",obj1.perimeter())
print("area of rectangle:",obj2.area(),"and","perimeter of rec",obj2.perimeter())
if(obj1.area()==obj2.area()):
    print("both rectangle have same area",obj1.area())
elif(obj1.area()>obj2.area()):
     print("first rectangle is greater",obj1.area())
else:
     print("second rectangle is greater",obj2.area())
    
    
