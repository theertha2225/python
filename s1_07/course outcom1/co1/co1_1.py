a=int(input("enter the year"))
b=int(input("enter the last year"))
i=a
while(i<b):
    def checkleap(i):
        if((i%400==0)or(i%100!=0)and(i%4==0)):
            print("leap year")
        else:
                print("non leap year")
    checkleap(i)
    i=i+1
