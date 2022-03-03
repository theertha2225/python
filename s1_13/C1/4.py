str="every day is a good day today is a good day"
a=str.split(" ")
print(a)
count=0
for i in range(0,len(a)):
    if(a[i]==x for x in str):
        count+=1
print("the occurence times of day is:",count)
