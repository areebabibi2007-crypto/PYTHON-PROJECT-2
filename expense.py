from utils import is_valid_amount

DATA_FILE = "data.txt"


def add_expense():
    print("\n===== Add New Expense =====")

    name = input("Enter Expense Name: ").strip().lower()
    amount = input("Enter Expense Amount: ").strip()

    if not is_valid_amount(amount):
        print("Invalid amount! Please enter numbers only.")
        return

    amount = float(amount)

    # Pehle purana data read karein
    expenses = {}
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if "," in line:
                    parts = line.split(",")
                    if len(parts) == 2:
                        item, amt = parts
                        expenses[item.strip().lower()] = float(amt.strip())
    except FileNotFoundError:
        pass

    # Unique name check: Agar name pehle se maujood hai toh amount add ho jayegi
    expenses[name] = expenses.get(name, 0.0) + amount

    # Clean data write karein taake repeat/duplicates na hon
    with open(DATA_FILE, "w") as file:
        for item, amt in expenses.items():
            file.write(f"{item},{amt}\n")

    print("Expense added successfully!")


def view_expenses():
    print("\n===== Expense List =====")

    try:
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No expenses found.")
            return

        for line in lines:
            line = line.strip()
            if "," in line:
                parts = line.split(",")
                if len(parts) == 2:
                    name, amount = parts
                    print(
                        f"Name: {name.strip().capitalize()} | Amount: ${float(amount.strip()):.2f}"
                    )

    except FileNotFoundError:
        print("No expenses found. Add some first!")