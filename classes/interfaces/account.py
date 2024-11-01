class AccountInterface : 
    
    def __init__(self, accountNumber, customerID, status, balance) :
        self.__balance = balance
        self.__accountNumber = accountNumber
        self.__accountHolderID = customerID
        
    #----------------------------------------------
    # Debit is to add money to the account
    # Credit is to remove money from the account
    #----------------------------------------------

    def debit(self, amount) :
        pass

    def credit(self, amount) :
        pass
    
    def getTransactionHistory(self) :
        pass

    def get_accountNumber(self):
        return self.__accountNumber

    def set_accountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def get_customerID(self):
        return self.__accountHolderID

    def set_customerID(self, customerID):
        self.__accountHolderID = customerID

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance