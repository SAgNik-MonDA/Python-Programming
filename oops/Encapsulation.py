class Account:
    def __init__(self,bal,acc):
        self.balence=bal
        self.account_no=acc
    def debit(self,amount):
        self.balence -= amount
        print("Rs.",amount,"was debit")
        print("Total balence:",self.balence)
    def credit(self,amount):
        self.balence += amount
        print("Rs.",amount,"was credit")
        print("Total balence:",self.balence)
        

acc1=Account(1000,1234)
acc1.debit(200)
acc1.credit(400)