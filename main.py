import pyfiglet
from banking.Transaction import Transaction
from banking.Balance_inquiry import Balance
from banking.Deposit import Deposit
from banking.Account import Account
from banking.database import BankDb
from tabulate import tabulate

ascii_banner = pyfiglet.figlet_format("My Bank", font="block")
print(ascii_banner)

def main():
    print("Welcome to My Bank!")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Transfer Money")
    print("4. History")
    print("5. get Balance")
    print("6. create Account")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        acc_id = input("Enter Account ID: ")
        amount = float(input("Enter Deposit Amount: "))
        pin = input("Enter your PIN: ")

        # instance
        deposit = Deposit(acc_id,amount, "Deposit",pin)
        deposit.deposit_Money()
        exit()

    elif choice == "2":
        acc_id = input("Enter Account ID: ")
        amount = float(input("Enter Withdrawal Amount: "))
        pin = input("Enter your PIN: ")

        deposit = Deposit(acc_id, amount, "Withdraw", pin)
        deposit.Withdraw()
        exit()

    elif choice == "3":
        sender_id = input("Enter Your Account ID: ")
        receiver_id = input("Enter To Account ID: ")
        amount = float(input("Enter Transfer Amount: "))

        transaction = Transaction(sender_id)
        transaction.transfer(receiver_id, amount)
        exit()

    elif choice == "4":
        accountid = input("enter your account number: ")
        db = BankDb()
        history_query = "SELECT * FROM transactions WHERE sender_id = ?"
        res = db.execute_query(history_query, (accountid,))

        if not res:
            print("Failed to fetch history!!!")
            exit()
        else:
            headers = ["ID", "Sender ID", "Type", "Receiver ID", "Amount", "Timestamp", "Transaction Hash"]
            print(tabulate(res, headers=headers, tablefmt="grid"))
        exit()

    elif choice == "5":
        accountid = input("enter your account number: ")
        Balance(accountid)

    elif choice == "6":
        name = input("enter your name: ")
        res = Account(name)
        print(res.get_user_account_details(res.accountId))

    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()