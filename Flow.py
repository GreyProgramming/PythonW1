num=int(input("What is your monthly take home pay?"))
if num>2000:
    print("A")
    if num>4000:
        print("C")
        if num>5000:
            print("I")
    else:
        print("F")
else:
    print("B")
    if num>1000:
        print("E")
    else:
        print("H")