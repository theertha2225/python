class bankaccount:
    def __init__(self):
        acno=float(input("enter account number:"))
        nameofholder=str(input("enter the name of account holder:"))
        typeofac=input("enter type of account:")
        self.balance=0
    def deposite(self):
        amount=float(input("enter amount to be deposited:"))
        self.balance+=amount
        print("amount deposited is",amount)
    def withdraw(self):
        amount=float(input("enter amount to be withdraw:"))
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("amount withdrew:",amount)
        else:
            print("balance is insufficient")
    def display(self):
        print("available balance:",self.balance)
s=bankaccount()
s.deposite()
s.withdraw()
s.display()
                 
