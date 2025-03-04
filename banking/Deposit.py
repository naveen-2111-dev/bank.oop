from database import BankDb


class Deposit:
    def __init__(self, AccountId, Amount):
        self.db = BankDb()
        self.accid = AccountId
        self.Amount = Amount

        self.deposit_Money()

    def deposit_Money(self):
        account = self.accid
        account_data = self.db.get_account_by_id(account)
        if account_data is None:
            print(f"Error: Account ID {self.accid} not found.")
            return

        account_id, name, balance = account_data

        if self.Amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        newBalance = balance + self.Amount

        Query_ToUpdate_DB = "UPDATE accounts SET balance=? WHERE account_id=?"
        res = self.db.execute_query(Query_ToUpdate_DB,(newBalance, self.accid))

        if res is not None:
            print(f"Deposit successful! New Balance: ${newBalance:.2f}")
        else:
            print("Error: Deposit failed. Account may not exist.")
