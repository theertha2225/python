class rectangle:
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area(self):
        a=self.length*self.bredth
        return a
    def perimeter(self):
        b=2*(self.length+self.bredth)
        return b
    a=int(input("enter length of 1 st rectangle"))
    b=int(input("enter bredth of 1 st rectangle"))
    c=int(input("enter length of 2nd rectangle"))
    d=int(input("enter bredth of 2nd rectangle"))
    obj1=rectangle(a,b)
    obj2=rectangle(c,d)
    print("area of rectangle",obj1.area(),"And","perimeter of rectangle",obj1.perimeter())
    print("area of rectangle",obj2.area(),"And","perimeter of rectangle",obj2.perimeter())
    if obj1.area()==obj2.area():
        print("both are same",obj1.area())
    elif obj1.area()>object.area():
        print("1st rectangle is greater ",obj1())
    else:
        print("2nd rectangle is greater",obj2())
