l1=[2,4,5,-43,67]
l2=[n for n in l1 if n>0]
print(l2)

l=[3,2,5,8,9,90]
l3=[x*x for x in l]
print(l3)

string="list of vowels"
l=["a","e","i","o","u"]
l4=[y for y in l if y in string]
print(l4)

string="Python"
l5=[ord(o)for o in string]
print(l5)
