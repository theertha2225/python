newFile = open("try.txt","w")
newFile.write("sonday\n monday\n tuesday \n wednessday\n thursday\n friday\n saturd
ay\n sunday")
newFile.close()
readFile = open("try.txt","r")
lines = readFile.readlines()
readFile.close()
oddFile = open("oddtry.txt","w")
forfor i in range(0,len(lines),2):
 oddFile.write(lines[i])
oddFile.close()
