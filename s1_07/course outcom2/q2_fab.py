n=int(input("enter the number of terms requird"))
a=0
b=1
c=0
if n<0:
    print("enter the positive number")
elif n==1:
    print("o")
else:
    print("the series is")
while c<n:
    print(a)
    temp=a+b
    a=b
    b=temp
    c=c+1
