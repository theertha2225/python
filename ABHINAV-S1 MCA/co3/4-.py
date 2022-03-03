class bankaccount:
    def __init__(self):
        accountno=float(input("enter account number :"))
        nameofholder=str(input("enter name of account holder:"))
        typeofaccount=str(input("enter type of account:"))
        self.balance=0
    def deposit(self):
            amount=float(input("enter amount to be deposited:"))
            self.balance+=amount
            print("amount depodited:",amount)
    def withdrw(self):
        amount=float(input("enter amount to be withdrw;"))
        if self.balance>=amount:
            self.balance+self.balance-amount
            print("amount withdraw:",amount)
        else:
            print("balance is insuficient:")
    def display(self):
        print("available balance:",self.balance)
s=bankaccount()
s.deposit()
s.withdrw()
s.display()
