class AccountInterface : 
    #-------------------
    # 
    #-------------------
    def __init__(self, accountNumber, customerID, status, balance) :
        self.__balance = balance
        self.__accountNumber = accountNumber
        self.__accountHolderID = customerID
        self.__status = status

    def deposit(self, amount) :
        pass

    def withdraw(self, amount) :
        pass

    def getBalance(self) :
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

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance