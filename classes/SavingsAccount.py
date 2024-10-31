from interfaces.account import AccountInterface

class SavingsAccount(AccountInterface):

    def __init__(self, balance, rate):
        super().__init__(balance)
        self.rate = rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def add_interest(self):
        self.balance += self.balance * self.rate

    def get_balance(self):
        return self.balance

    def get_rate(self):
        return self.rate

    def __str__(self):
        return "Savings account: balance = " + str(self.balance) + ", rate = " + str(self.rate)