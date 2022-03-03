names=[]
n=input("enter number of name:")
a_count=0
for i in range(int(n)):
    name=input("input a name:")
    name.append(name)
for name in names:
    count=name.count("a")
    a_count+=count
print(a_count)    
