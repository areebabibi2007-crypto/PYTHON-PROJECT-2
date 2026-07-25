DATA_FILE = "data.txt"


def show_report():
    print("\n========== EXPENSE REPORT ==========")

    try:
        with open(DATA_FILE, "r") as file:
            expenses = file.readlines()

            if len(expenses) == 0:
                print("No expenses available.")
                return

            total = 0
            count = 0

            print("\nExpense Details")
            print("-" * 35)

            for expense in expenses:
                name, amount = expense.strip().split(",")
                amount = float(amount)

                print(f"{name:<20} Rs. {amount:.2f}")

                total += amount
                count += 1

            average = total / count

            print("-" * 35)
            print(f"Total Expenses : {count}")
            print(f"Total Amount   : Rs. {total:.2f}")
            print(f"Average Expense: Rs. {average:.2f}")
            print("=" * 35)

    except FileNotFoundError:
        print("No expense data found.")