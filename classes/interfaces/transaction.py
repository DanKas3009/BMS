
class Transaction:
    def __init__(self, transaction_id, transaction_date, transaction_amount, transaction_type, transaction_category, transaction_description):
        self.__transaction_id = transaction_id
        self.__transaction_date = transaction_date
        self.__transaction_amount = transaction_amount
        self.__transaction_type = transaction_type
        self.__transaction_category = transaction_category
        self.__transaction_description = transaction_description

    def processTransaction(self):
        pass
    def reverseTransaction(self):
        pass
    
    def get_transaction_id(self):
        return self.__transaction_id

    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def get_transaction_date(self):
        return self.__transaction_date

    def set_transaction_date(self, transaction_date):
        self.__transaction_date = transaction_date

    def get_transaction_amount(self):
        return self.__transaction_amount

    def set_transaction_amount(self, transaction_amount):
        self.__transaction_amount = transaction_amount

    def get_transaction_type(self):
        return self.__transaction_type

    def set_transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def get_transaction_category(self):
        return self.__transaction_category

    def set_transaction_category(self, transaction_category):
        self.__transaction_category = transaction_category

    def get_transaction_description(self):
        return self.__transaction_description

    def set_transaction_description(self, transaction_description):
        self.__transaction_description = transaction_description