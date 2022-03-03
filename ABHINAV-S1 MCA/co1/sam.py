str="every day is a good day today is a good day"
l=[]
l=str.split(" ")
lset=set(l)
print(lset)
for i in lset:
    print(i,'occur',l.count(i),"times")

   

