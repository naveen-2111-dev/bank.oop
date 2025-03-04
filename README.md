# Simple Banking App

## Overview
A **simple banking application** built using **Python** that allows users to perform basic banking operations such as account creation, balance inquiry, deposits, and withdrawals. The project follows **Object-Oriented Programming (OOP)** principles and utilizes **SQLite3** for data storage.

## Features
- ✅ Create a new bank account
- 💰 Deposit money into an account
- 💸 Withdraw money from an account
- 📊 Check account balance
- 📜 View transaction history
- 🔒 Secure transaction hashes using SHA-256

## Tech Stack
- **Python** - Core programming language
- **SQLite3** - Lightweight database for storing accounts and transactions
- **Pandas** - Used for handling and displaying financial data
- **OOP Principles** - Ensures modularity and maintainability

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/naveen-2111-dev/bank.oop.git
   cd bank.oop
   ```
2. **Create a virtual environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   python main.py
   ```

## Directory Structure
```
├─ README.md
├─ banking/
│  ├─ Account.py
│  ├─ Balance_inquiry.py
│  ├─ Deposit.py
│  ├─ Transaction.py
│  ├─ __init__.py
│  ├─ bank.db
│  └─ database.py
├─ main.py
├─ requirements.txt
└─ utils/
   ├─ __init__.py
   └─ utils.py
```

## Security
- 🔐 **SHA-256 hashing** is used for transaction security.
- ✅ Input validation is implemented to prevent invalid transactions.

