from .interfaces.account import AccountInterface

class SavingsAccount(AccountInterface):

    def __init__(self, accountNumber, customerID, status, balance, rate):
        super().__init__(accountNumber, customerID, status,balance)
        self.__rate = rate

    def debit(self, amount):
        self.set_balance(self.get_balance() + amount)
        return self.get_balance()

    def credit(self, amount):
        self.set_balance(self.get_balance() - amount)
        return self.get_balance()


    def get_interest(self):
        self.set_balance(self.get_balance() * self.__rate)

    def get_rate(self):
        return self.__rate

    def __str__(self):
        return "Savings account: balance = " + str(self.get_balance()) + ", rate = " + str(self.__rate)