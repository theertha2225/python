s=int(input("enter the year:"))
print("leap year between 2021 and ",s)
for i in range(2021,s,1):
    if(i%4==0) and (i%100!=0) or (i%400==0):
      print(i)