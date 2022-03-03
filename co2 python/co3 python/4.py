class bankaccount:
    def __init__(self):
        accountnumber=float(input("enter account number"))
        accountname=str(input("enter acoount name"))
        accounttype=str(input("type of account"))
        self.balance=0
        print("------------------------")
    def deposit(self):
        amount=float(input("enter amount to deposit"))
        self.balance+=amount
        print("amount deposited is",amount)
        print("------------------------")
    def withdraw(self):
        amount=float(input("enter amount to witdraw"))
        self.balance-=amount
        print("amount withdrawn is",amount)
        print("------------------------")
    def display(self):
        print("avilable balance:",self.balance)
        print("------------------------")

s=bankaccount()
s.deposit()
s.withdraw()
s.display()

