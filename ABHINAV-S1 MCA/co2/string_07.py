def str():
    string=input("enter a word")
    last=string[-3]
    if(last=="ing"):
        string+="ly"
        print(string)
    else:
        string+="ing"
        print(string)
str()
