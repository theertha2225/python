class time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s
    def __add__(self,other):
        self.__hour+=other.__hour
        self.__minute+=other.__minute
        self.__second+=other.__second
        if(self.__second>=60):
            extra_minute=int(self.__second/60)
            self.__second=self.__second%60
            self.__minute+=extra_minute
        if(self.__minute>=60):
            extra_hour=int(self.__minute/60)
            self.__minute=self.__minute%6
            self.__hour+=extra_hour
        return " Hour(s):"+str(self.__hour)+" : Minute(s):"+str(self.__minute)+" : second(s): "+str(self.__second)
ob1=time(5,40,30)
ob2=time(3,40,15)
print(ob2+ob1)
