
fileopen=open("test.txt","r")
filewrite=open("test2.txt","w")
for x in fileopen:
    print(x,file=filewrite.replace("e","*")+"w")
