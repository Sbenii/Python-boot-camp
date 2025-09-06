class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def display(self):
        return f"Account owner: {self.name}\nAccount balance: {self.balance}"
    def deposit(self,depo):
        self.balance=self.balance+depo
        return "Deposit accepted"
    def withdrawal(self,withdraw):
        if withdraw<=self.balance:
            print("Withdrawal accepted")
            self.balance=self.balance-withdraw
        else:
            return "Funds unavailable"

acct1 = Account('Jose',100)
print(acct1.display())
print(acct1.name)
print(acct1.balance)
print(acct1.deposit(50))
acct1.withdrawal(75)
print(acct1.withdrawal(500))