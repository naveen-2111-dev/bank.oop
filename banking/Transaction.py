from banking.database import BankDb
from utils import Utils
import time


class Transaction:
    def __init__(self, Id):
        self.db = BankDb()
        det = self.db.get_account_by_id(Id)

        if not det:
            print("Invalid account ID")
            return

        if len(det) != 4:
            print("Error: Unexpected database response format.")
            return

        account_id, name,balance, pin = det
        self.bal = balance
        self.id = account_id

    def transfer(self, to_address, amount):
        if self.bal < amount:
            print("Insufficient balance")
            return

        res = self.db.get_account_by_id(to_address)
        if not res:
            print("Recipient account not found")
            return

        account_id, name,balance, pin = res

        new_balance = balance + amount
        user_bal = self.bal - amount

        update_query = "UPDATE accounts SET balance=? WHERE account_id=?"

        update_user_bal = self.db.execute_query(update_query, (user_bal, self.id))
        if update_user_bal is None:
            print("Payment failed while deducting sender balance")
            return

        update_res = self.db.execute_query(update_query, (new_balance, to_address))
        if update_res is None:
            print("Payment failed while crediting receiver balance")
            return

        txhash = Utils.transactionhash()
        self.history(self.id, "transfer", to_address, amount, time.time(), txhash)

        print(f"Payment success! Transferred ${amount} to {to_address} | {name}")

    def history(self, sender_id, tx_type, receiver_id, amount, timestamp, tx_hash):
        history_update_query = """
        INSERT INTO transactions(sender_id, tx_type, receiver_id, amount, timestamp, tx_hash)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        res = self.db.execute_query(history_update_query,
                                    (sender_id, tx_type, receiver_id, amount, timestamp, tx_hash))

        if res is None:
            print("Error: Transaction history not saved.")
            return False
        else:
            print("Transaction history saved successfully.")
            return True
