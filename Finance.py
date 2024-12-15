import sqlite3
from tabulate import tabulate

# Database setup
def init_db():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            income REAL,
            expense REAL
        )
    ''')
    conn.commit()
    conn.close()

# Transaction operations
def add_transaction(date, description, income, expense):
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, description, income, expense) 
        VALUES (?, ?, ?, ?)
    ''', (date, description, income, expense))
    conn.commit()
    conn.close()

def view_transactions():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT date, description, COALESCE(income, ''), COALESCE(expense, '') FROM transactions")
    records = cursor.fetchall()
    conn.close()
    return records

def get_balance():
    conn = sqlite3.connect("finance_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(COALESCE(income, 0)) - SUM(COALESCE(expense, 0)) FROM transactions")
    balance = cursor.fetchone()[0]
    conn.close()
    return balance if balance is not None else 0

# User interface functions
def display_menu():
    print("\nOptions:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Balance")
    print("4. Exit")

def handle_add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    income_input = input("Enter income (leave blank if none): ")
    expense_input = input("Enter expense (leave blank if none): ")
    income = float(income_input) if income_input else None
    expense = float(expense_input) if expense_input else None
    add_transaction(date, description, income, expense)
    print("Transaction added successfully.")

def handle_view_transactions():
    transactions = view_transactions()
    balance = get_balance()
    if transactions:
        print("\nTransaction History:")
        print(tabulate(transactions, headers=["Date", "Description", "Income", "Expense"], tablefmt="grid"))
        print(f"\nRemaining Balance: {balance:.2f}")
    else:
        print("No transactions found.")

def handle_view_balance():
    balance = get_balance()
    print(f"\nCurrent Balance: {balance:.2f}")

# Main program loop
def main():
    init_db()
    print("Welcome to Personal Finance Tracker")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            handle_add_transaction()
        elif choice == "2":
            handle_view_transactions()
        elif choice == "3":
            handle_view_balance()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
