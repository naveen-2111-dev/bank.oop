import sqlite3

class BankDb:
    def __init__(self, dbName="bank.db"):
        self.connection = sqlite3.connect(dbName)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts(
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
        """)

        self.connection.commit()

    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()
            return None

    def get_account_by_id(self, account_id):
        self.cursor.execute("""
        SELECT account_id, name, balance 
        FROM accounts 
        WHERE account_id = ?;
        """, (account_id,))

        return self.cursor.fetchone()

    def close_connection(self):
        self.connection.close()