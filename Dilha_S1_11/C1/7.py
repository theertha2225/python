l1=[1,3,6,8,9]
l2=[2,4,7,9,0]
print(len(l1))
print(len(l2))
if(len(l1)==len(l2)):
    print("same length")
else:
    print("not same length")
print(sum(l1))
print(sum(l2))
if(sum(l1)==sum(l2)):
    print("sum is same ")
else:
    print("sum is not same")
l3=[x for x in l1 if x in l2]
print("common in both list",l3)

