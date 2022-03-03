def char():
    from collections import Counter
    s=input("enter a string:")
    fre=Counter(s)
    print("the character frequency of the given string is:",str(fre))
char()
