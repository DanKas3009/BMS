from .interfaces.account import AccountInterface
from .interfaces.transaction import Transaction

class WithdrawTransaction(Transaction):
    def __init__(self, transaction_id, transaction_date, transaction_amount, transaction_type, transaction_category, transaction_description):
        super().__init__(transaction_id, transaction_date, transaction_amount, transaction_type, transaction_category, transaction_description)
    
    def processTransaction(self, account: AccountInterface):
        account.credit(self.get_transaction_amount()) 
        # add transaction to transaction history
        # Add database transaction
        print("Processing deposit transaction")
    
    def reverseTransaction(self,  account: AccountInterface):
        account.debit(self.get_transaction_amount()) # return the money back to the account
        # reverse transaction
        print("Reversing deposit transaction")