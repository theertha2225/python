class rectangle:
    __length=0
    __width=0
    __area=0
 def__init__(self,l,w):
     self.__length=l
     self.__width=w
 def area(self):
     self.__area=self.__length*self.__width
 def__gt__(self,other):
     if(self.__area>other.__area):
        return true
    else:
        return false
ob1=rectangle(3,4)
ob1.area()
ob2=rectangle(4,5)
ob2.area()
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")
