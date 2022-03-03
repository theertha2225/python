def fibno():
    n1=0;n2=1
    c=0
    if(a<=0):
        print("enter positive integer")
    elif(a==1):
        print("0")
    else:
        print("the series is:")
        while(c<a):
            print(n1)
            temp=n1+n2
            n1=n2
            n2=temp
            c+=1
a=int(input("enter the number"))
fibno()
      
