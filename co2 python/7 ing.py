def ing():
    str=input("enter a string")
    last=str[-3:]
    if(last=="ing"):
        str+="ly"
    else:
        str+="ing"
    print(str)
ing()
