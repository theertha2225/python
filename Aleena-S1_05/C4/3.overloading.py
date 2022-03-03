class rectangle :
 __length=0
 __width=0
 __area=0
 def __init__(self,l,w):
  self.__length=l
  self.__width=w
 def area(self):
  self.__area=self.__length*self.__width
 def __gt__(self,other):
     if (self.__area>other.__area):
      return True
     else :
      return False
ob1=rectangle(3,4)
ob1.area()
ob2=rectangle(5,7)
ob2.area()
if (ob1>ob2):
 print("ob1 is greater thab ob2")
else:
 print("ob2 is greater than ob1") 
