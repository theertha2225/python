def fib():
    n=int(input("enter a number"))
    n1=0
    n2=1
    e=0
    if(n<0):
        print("enter the +ve integer")
    elif(n==1):
        print("o")
    else:
        print ("the series is")
    while(e<n):
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        e+=1
fib()
