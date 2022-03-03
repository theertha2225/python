l1=[2,4,6,8,10]
l2=[2,3,5,6,8,7,9]
if(len(l1)==len(l2)):
    print("both are same ")
else:
    print("both are not same")
if(sum(l1)==sum(l2)):
    print("having same length")
else:
    print("lengths are different")
l3=[x for x in l1 if x in l2]
print("common in both list",l3)
