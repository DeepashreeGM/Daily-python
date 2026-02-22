class BankAccount:
    bank_name="National Bank"
    def __init__(self):
        self.account_holder=None
        self.balance=0
    def deposite(self,amount):
        self.balance=self.balance+amount
        
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def display(self):
         print("Account holder,",self.account_holder)
         print("Balance,",self.balance)
a1=BankAccount()
a1.account_holder="Deepa"
a1.balance=80000
a1.deposite(10000)
a1.withdraw(20000)
print(a1.balance)
a1.display()
a2=BankAccount()
a2.account_holder="Deepa"
a2.balance=80000
a2.deposite(20000)
a2.withdraw(50000)
print(a2.balance)
a1.display()