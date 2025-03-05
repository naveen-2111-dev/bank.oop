from banking.database import BankDb
from utils import Utils
import time

class Deposit:
    def __init__(self, AccountId, Amount, choice, User_pin):
        self.db = BankDb()
        self.accid = AccountId
        self.Amount = Amount
        self.new_balance = None
        self.userpin = User_pin

        if choice.lower() == "withdraw":
            self.Withdraw()
        elif choice.lower() == "deposit":
            self.deposit_Money()
        else:
            print("Invalid choice! Please select 'Withdraw' or 'Deposit'.")
            return

        if self.new_balance is not None:
            Query_ToUpdate_DB = "UPDATE accounts SET balance=? WHERE account_id=?"
            res = self.db.execute_query(Query_ToUpdate_DB, (self.new_balance, self.accid))

            if res is not None:
                print(f"Transaction successful! New Balance: ${self.new_balance:.2f}")
            else:
                print("Error: Transaction failed. Account may not exist.")

    def Withdraw(self):
        from banking.Transaction import Transaction
        if self.Amount <= 0:
            print("Error: Amount cannot be zero or negative.")
            return

        res = self.db.get_account_by_id(self.accid)
        if res is None:
            print("Error: Unable to find the account number.")
            return

        account_id, name, balance, pin = res

        if int(self.userpin) != int(pin):
            print("Error: Invalid PIN.")
            return

        if balance < self.Amount:
            print("Error: Insufficient balance.")
            return

        txhash = Utils.transactionhash()
        tx = Transaction(account_id)
        tx.history(account_id, "withdrawal", account_id, self.Amount, int(time.time()), txhash)
        self.new_balance = balance - self.Amount

    def deposit_Money(self):
        from banking.Transaction import Transaction
        res = self.db.get_account_by_id(self.accid)
        if res is None:
            print(f"Error: Account ID {self.accid} not found.")
            return

        account_id, name, balance, pin = res

        if int(self.userpin) != int(pin):
            print("Error: Invalid PIN.")
            return

        if self.Amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        txhash = Utils.transactionhash()
        tx = Transaction(account_id)
        tx.history(account_id, "deposit", account_id, self.Amount, int(time.time()), txhash)
        self.new_balance = balance + self.Amount
