def string():
    from collections import Counter
    s=input("enter a string")
    fre=Counter(s)
    print("the character frequency in given string is",str(fre))
string()
