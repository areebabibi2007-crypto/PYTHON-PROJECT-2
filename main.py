import os

# Exact path handle karne ke liye
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.txt")

def show_report():
    print("\n===== Expense List =====")
    
    expenses = []
    total_amount = 0.0
    seen_expenses = set()  # Yeh duplicates ko roke ga

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if "," in line:
                    # Agar bilkul same line dobara aaye toh skip kar do
                    if line in seen_expenses:
                        continue
                    seen_expenses.add(line)
                    
                    parts = line.split(",")
                    if len(parts) == 2:
                        name, amount = parts
                        amt = float(amount.strip())
                        expenses.append((name.strip().capitalize(), amt))
                        total_amount += amt

        if not expenses:
            print("No expenses found.")
            return

        for name, amt in expenses:
            print(f"Name: {name:<12} | Amount: ${amt:.2f}")

        print("-----------------------------------")
        total_count = len(expenses)
        avg_expense = total_amount / total_count if total_count > 0 else 0.0

        print(f"Total Expenses : {total_count}")
        print(f"Total Amount   : ${total_amount:.2f}")
        print(f"Average Expense: ${avg_expense:.2f}")
        print("===================================")

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def add_expense():
    print("\n===== Add Expense =====")
    name = input("Enter expense name: ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
        with open(DATA_FILE, "a") as file:
            file.write(f"{name},{amount}\n")
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")

def main():
    while True:
        print("\n===================================")
        print("      EXPENSE TRACKER SYSTEM       ")
        print("===================================")
        print("1. Add Expense")
        print("2. View Expenses / Report")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_report()
        elif choice == "3":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()