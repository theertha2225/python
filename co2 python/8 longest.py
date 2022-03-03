l=[]
n=int(input("how many words entered"))
print("enter word")
for i in range(n):
    l.append(len(input()))
print("the longest word with size----"+str(max(l)))
