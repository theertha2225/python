names=[]
n=input("enter the names")
a_count=0
for i in range(int(n)):
    name=input("input names")
    names.append(name)
for name in names:
    count=name.count("a")
    a_count=count+1
    print(a_count)
