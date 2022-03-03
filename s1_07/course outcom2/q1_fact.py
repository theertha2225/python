def fact(i):
    i=i+1
    f=1
    j=1
    for j in range(1,i):
        f=f*j
    return f
n=int(input("enter the num"))
a=fact(n)
print(a)
    
  
    
