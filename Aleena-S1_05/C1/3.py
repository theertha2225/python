l1=[1,20,-34,50,-67]
print(l1)
l2=[n for n in l1 if n>0]
print(l2)

l3=[x*x for x in l1]
print(l3)

str="hello world hai world"
l=["a","e","i","o","u"]
l4=[y for y in l if y in str]
print(l4)

string="python"
l5=[ord(o) for o in string]
print(l5)
