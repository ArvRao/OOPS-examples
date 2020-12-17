class BankAccount:
    def __init__(self):
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        
        else:
            print("Your amount is low.")

    def print_balance(self):
        return self.balance

account = BankAccount()

account.deposit(100)
account.deposit(2020)
account.deposit(50) # deposit $2170 to your account

print(account.print_balance())

account.withdraw(1000) #withdraw $1000 back from your account

print(account.print_balance())

account.withdraw(1200) #We try to withdraw $1200, but since your balance is lower than expected withdrawal cash, it's unsuccessful transaction.
