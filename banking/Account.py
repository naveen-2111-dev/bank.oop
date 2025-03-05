from tabulate import tabulate
import random

from banking.database import BankDb


class Account:
    def __init__(self, Holder_name, balance=0.0):
        self.db = BankDb()
        self.accountId = random.randint(10**9, 10**10 - 1)
        self.Holder_name = Holder_name
        self.balance = balance
        self.pin = random.randint(1000, 9999)

        result = self.db.execute_query(
            "INSERT INTO accounts (account_id, name, balance, pin) VALUES (?, ?, ?, ?)",
            (self.accountId, self.Holder_name, self.balance, self.pin)
        )

        if result is not None:
            print(f"Account created successfully! Account ID: {self.accountId}")
        else:
            print("Account creation failed. Please try again.")

    def get_user_account_details(self, Id):
        accountData = self.db.get_account_by_id(Id)

        if accountData:
            account_id, name, balance, pin = accountData

            data = [
                ["Account ID", account_id],
                ["Name", name],
                ["Balance", f"${balance:.2f}"],
                ["pin", pin]
            ]

            return tabulate(data, tablefmt="grid")
        else:
            return "Account not found."
