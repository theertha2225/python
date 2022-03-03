def fact(p):
    i=1
    f=1
    while(i<=p):
        f=f*i
        i=i+1
    return f
n=int(input("enter the number:"))   
f=fact(n)    
print(f)   
