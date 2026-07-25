# 💰 Expense Tracker System (Python)

A console-based Expense Tracker application written in Python. It allows users to log daily expenses, save them into a local file (data.txt), and generate formatted expense reports with calculated total expenditure.

---

## 📌 Features
- *Add Expense:* Easily log expense name and amount.
- *Data Persistence:* Automatically stores expenses in data.txt.
- *View Expense Report:* Displays tracked items with proper layout and calculates *Total Amount*.
- *Input Validation:* Prevents invalid expense values.

---

## 🛠️ Project Structure
text
python project 2/
│── main.py          # Entry point & CLI menu
│── expense.py       # Functions for adding expenses
│── show_report.py   # Reading & displaying reports
│── utils.py        # Helper validations
│── data.txt         # Data file storing expenses
└── README.md        # Documentation


---

## 🚀 How to Run
Run the main file using Python:
bash
python main.py


---

## 📊 Terminal Output Preview

text
====================================
      EXPENSE TRACKER SYSTEM
====================================
1. Add Expense
2. View Expenses / Report
3. Exit
------------------------------------
Enter your choice (1-3): 1

--- Add Expense ---
Enter expense name: Food
Enter amount: 500
Expense added successfully!

====================================
      EXPENSE TRACKER SYSTEM
====================================
1. Add Expense
2. View Expenses / Report
3. Exit
------------------------------------
Enter your choice (1-3): 2

====================================
          Expense List
====================================
Name: Food         Amount: $500.00
Name: Transport    Amount: $250.00
Name: Shopping     Amount: $1200.00
------------------------------------
Total Amount  : $1950.00
Average Spend : $650.00
====================================