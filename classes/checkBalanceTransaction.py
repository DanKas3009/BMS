from .interfaces.account import AccountInterface
from .interfaces.transaction import Transaction

class CheckBalanceTransaction(Transaction):
    def __init__(self, transaction_id, transaction_date, transaction_amount, transaction_type, transaction_category, transaction_description):
        super().__init__(transaction_id, transaction_date, transaction_amount, transaction_type, transaction_category, transaction_description)
    
    def processTransaction(self, account: AccountInterface):
        print("Processing deposit transaction")
        return account.get_balance()
        # add transaction to transaction history
        # Add database transaction