from database import BankDb
from tabulate import tabulate

class Balance:
    def __init__(self, Id):
        self.db = BankDb()
        self.AccountId = Id

        result = self.db.get_account_by_id(Id)
        if result is None:
            print(f"No data found for Account ID: {Id}")
            return

        account_id, name, balance = result

        data = [
            ["Account ID", account_id],
            ["Name", name],
            ["Balance", f"${balance:.2f}"]
        ]

        print(tabulate(data, tablefmt="grid"))
