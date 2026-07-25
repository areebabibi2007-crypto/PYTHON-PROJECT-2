# 💰 EXPENSE TRACKER SYSTEM

## Python Programming Project 2

A console-based Expense Tracker application developed using Python
as part of the Industrial Training Kit – Project 2.

---

# 📌 PROJECT INFORMATION

*Project Name:* Expense Tracker System

Submitted by: Areeba Bibi

*Project Number:* Project 2

*Batch:* 2026

*Programming Language:* Python 3

*Project Type:* Console-Based Application

*Organization:* DecodeLabs

---

# 📖 PROJECT OVERVIEW

Expense Tracker is a Python console application designed to help
users record and manage their daily expenses.

The application allows users to enter expense names and amounts,
save the records in a text file, view all saved expenses, and
generate an expense report.

The project focuses on data accumulation, mathematical operations,
and processing numerical data.

---

# 🎯 PROJECT GOAL

The main goal of this project is to create a program where users
can enter expense amounts and the program calculates the total
amount spent.

Example:

Food = $500
Transport = $250
Shopping = $1200

Total Spent = $1950

---

# 🎯 PROJECT OBJECTIVES

The main objectives of this project are:

- To practice Python programming.
- To understand user input.
- To use mathematical calculations.
- To understand accumulators.
- To practice functions.
- To practice file handling.
- To store data permanently.
- To generate an expense report.
- To improve programming and problem-solving skills.

---

# ✨ FEATURES

The Expense Tracker System provides the following features:

### 1. Add Expense

Users can enter:

- Expense name
- Expense amount

The expense is then saved in the data file.

### 2. View Expenses

Users can view all previously saved expenses.

### 3. Expense Report

The application automatically displays:

- Total number of expenses
- Total amount spent
- Average expense

### 4. File Storage

All expenses are stored in:

data.txt

### 5. Input Validation

The program checks whether the entered expense amount is a
valid number.

### 6. Simple Menu

The application provides three choices:

1. Add Expense
2. View Expenses & Expense Report
3. Exit

---

# 📂 PROJECT STRUCTURE

```text
Expense_Tracker/
│
├── main.py
├── expense.py
├── report.py
├── utils.py
├── data.txt
├── README.md
└── requirements.txt

# 🖥️ PROGRAM OUTPUT

The following is the complete sample output of the Expense Tracker System.

```text
========================================
       EXPENSE TRACKER SYSTEM
========================================
1. Add Expense
2. View Expenses & Expense Report
3. Exit

Enter your choice (1-3): 1

===== Add New Expense =====

Enter Expense Name: Food
Enter Expense Amount: 500

Expense added successfully!


========================================
       EXPENSE TRACKER SYSTEM
========================================
1. Add Expense
2. View Expenses & Expense Report
3. Exit

Enter your choice (1-3): 1

===== Add New Expense =====

Enter Expense Name: Transport
Enter Expense Amount: 250

Expense added successfully!


========================================
       EXPENSE TRACKER SYSTEM
========================================
1. Add Expense
2. View Expenses & Expense Report
3. Exit

Enter your choice (1-3): 1

===== Add New Expense =====

Enter Expense Name: Shopping
Enter Expense Amount: 1200

Expense added successfully!


========================================
       EXPENSE TRACKER SYSTEM
========================================
1. Add Expense
2. View Expenses & Expense Report
3. Exit

Enter your choice (1-3): 2

========== EXPENSES & REPORT ==========

----- View Expenses -----

Name: Food       | Amount: $500.00
Name: Transport  | Amount: $250.00
Name: Shopping   | Amount: $1200.00

----------------------------------------

----- Expense Report -----

Total Expenses  : 3
Total Amount    : $1950.00
Average Expense : $650.00

========================================


========================================
       EXPENSE TRACKER SYSTEM
========================================
1. Add Expense
2. View Expenses & Expense Report
3. Exit

Enter your choice (1-3): 3

Thank you for using Expense Tracker.
Goodbye!