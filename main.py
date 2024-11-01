from classes.checkBalanceTransaction import CheckBalanceTransaction
from classes.depositTransaction import DepositTransaction
from classes.withdrawTransaction import WithdrawTransaction
from classes.SavingsAccount import SavingsAccount

def main():
    # Create a savings account
    account = SavingsAccount(1, 1, "Active", 100, 0.05)
    print(account)
    
    # Create a deposit transaction
    deposit = DepositTransaction(1, "2020-01-01", 100, "Deposit", "Income", "Deposit transaction")
    deposit.processTransaction(account)
    print(account)
    
    # Create a withdraw transaction
    withdraw = WithdrawTransaction(2, "2020-01-02", 50, "Withdraw", "Expense", "Withdraw transaction")
    withdraw.processTransaction(account)
    print(account)
    
    # Create a check balance transaction
    check_balance = CheckBalanceTransaction(3, "2020-01-03", 0, "Check Balance", "Income", "Check balance transaction")
    balance = check_balance.processTransaction(account)
    print("Account balance: ", balance)
    
    # Reverse the withdraw transaction
    withdraw.reverseTransaction(account)
    print(account)
    
    # Get the interest
    account.get_interest()
    print(account)

if __name__ == "__main__":
    main()