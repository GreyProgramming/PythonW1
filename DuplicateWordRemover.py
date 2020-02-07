    #ask for a message
msg=input("Please input a message: ")

    #compile message into list of words
words=msg.split()

    #join the words as a unique list
words2 = set(words)

    #print
print(words2)