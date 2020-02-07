num = {1: "one", 2: "two",3: "three",4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine"}
xten = {1: "eleven",2: "twelve",3: "thirteen",4: "fourteen",5: "fifteen",6: "sixteen",7: "seventeen",8: "eighteen",9: "nineteen"}
tens = {1: "ten",2: "twenty",3: "thirty",4: "fourty",5: "fifty",6: "sixty",7: "seventy",8: "eighty",9: "ninety"}

raw = int(input("Feed me four digits please! "))
edit = raw

    # is it 4 digits?
while len(str(edit)) == 4:
    thous = edit//1000
    edit = edit%1000
    print(num[thous],"thousand")

    #is it 3 digits?
while len(str(edit)) == 3:
    Hund = edit//100
    edit = edit%100
    print(num[Hund],"hundred")

    #if it is 2 digits, is it a multiple of 10?
while len(str(edit)) == 2:
    if edit%10==0:
        place=edit//10
        print(tens[place])
        break
    #
    else:
        if edit//10==1:
            place=edit%10
            print(xten[place])
            break
        else:
            tendig = edit // 10
            place = edit % 10
            print(tens[tendig], num[place])
            break

while len(str(edit)) == 1:
    print(num[edit])
    break