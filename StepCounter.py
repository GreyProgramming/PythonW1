potential = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
steps = int(input("How many steps do you want? "))
stepcount = ""
i = 0
while i<steps:
    if i<1:
        stepcount += str(potential[i])
    else:
        stepcount += ","+ str(potential[i])
    print(stepcount+".")
    i+=1
