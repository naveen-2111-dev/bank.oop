from banking.database import BankDb

class Balance:
    def __init__(self, Id):
        self.db = BankDb()
        self.AccountId = Id

        result = self.db.get_account_by_id(Id)
        if result is None:
            print(f"No data found for Account ID: {Id}")
            return

        account_id, name, balance, pin = result

        message = (
            f"The account holder's name is {name}, "
            f"and the account number is {account_id}. "
            f"The current balance is ${balance:.2f}."
        )

        print(message)

# balance = Balance(1605271366)
