fresh= "Y"
file=open('Records.csv','a')

while fresh== "Y" or fresh== "y":
    reg = int(input("Registration number: "))
    name = str(input("Full name: "))
    add = str(input("address: "))
    save = str(input("Do you want to save this record? (Y/N) "))
    if save == "Y" or save=="y":
        print(reg,name,add,sep=",",file=file)
        print("Record saved.")
    else:
        print("Record not saved.")
    fresh=str(input("Do you want to add another record? (Y/N) "))
print("Thank you for using recordsaver.")