alpha=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
msg = input("Input a message here, please: ")

# find the number of characters in the set
x=0
while x<len(msg):
    if ord(msg[x])>=65 and ord(msg[x])<=90:
        alpha[ord(msg[x])-65]+=1
    if ord(msg[x])>=97 and ord(msg[x])<=122:
        alpha[ord(msg[x])-97]+=1
    x+=1

#Print the characters in set
x=0
while x<len(alpha):
    if alpha[x]!=0:
        print(chr(x+65),"=",alpha[x])
    x+=1