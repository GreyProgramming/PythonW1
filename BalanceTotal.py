class Bank:
    current = 0
    savings = 0
    isa = 0
    def T(self):
        return(self.current + self.savings + self.isa)
    def Balance(self):
        print("Your total is:")
        print(self.current+self.savings+self.isa)
    def assign(self,c,s,i):
        self.current=c
        self.savings=s
        self.isa=i

BarcTot = Bank()
BarcTot.assign(1000.10,100,2000)
print("Barclays")
BarcTot.Balance()

NatTot = Bank()
NatTot.assign(100,100,0)
print("Natwest")
NatTot.Balance()

HaliTot = Bank()
HaliTot.assign(100,0,0)
print("Halifax")
HaliTot.Balance()

print("Total is:",BarcTot.T()+NatTot.T()+HaliTot.T())