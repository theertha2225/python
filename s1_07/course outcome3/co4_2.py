class bankac:
    def __init__(self):
        acc_no=float(input("enter the account number:"))
        name=str(input("enter the name:"))
        type_of_acc=str(input("enter the type of account"))
        self.balance=0
    def deposit(self):
        amount=float(input("enter the amount to be deposited:"))
        self.balance+=amount
        print("amount deposited is",amount)
    def withdraw(self):
        amount=float(input("the withdrawn amount is:"))
        if self.balance>=amount:
            
            self.balance=self.balance-amount
            print("amount withdrew",amount)
        else:
            print("balance is insufficient")
    def display(self):
        print("available balance:",self.balance)

    
s=bankac()
s.deposit()
s.withdraw()
s.display()
