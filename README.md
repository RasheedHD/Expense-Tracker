# Expense Tracker

A simple command-line expense tracker built with Python. This application allows users to manage their expenses efficiently by adding, updating, deleting, and viewing expenses, along with generating summaries and setting monthly budgets.

---

## 🚀 Features

### Core Features

* Add an expense with description, amount, and category
* Update an existing expense
* Delete an expense
* View all expenses
* View expenses filtered by category
* View total expenses
* View monthly expense summary (current year)

### Additional Features

* Set monthly budgets
* Get warnings when exceeding budget
* Store data persistently using CSV files

---

## 🛠️ Technologies Used

* Python 3
* `argparse` for command-line interface
* `csv` for data storage
* `datetime` for handling dates

---

## 📂 Project Structure

* `expenses.csv` → Stores all expense records
* `budget.csv` → Stores monthly budget limits
* `main.py` (your script) → Contains all application logic

---

## ⚙️ Installation & Setup

1. Make sure Python 3 is installed:

   ```bash
   python --version
   ```

2. Clone or download the project.

3. Ensure the following files exist in the same directory:

   * `expenses.csv`
   * `budget.csv`

4. Run the program using:

   ```bash
   python main.py <command> [options]
   ```

---

## 📌 Usage

### ➕ Add Expense

```bash
python main.py add --description "Lunch" --amount 20 --category Food
```

---

### 📋 List Expenses

```bash
python main.py list
```

Filter by category:

```bash
python main.py list --category Food
```

---

### ✏️ Update Expense

```bash
python main.py update --id 1 --description "Dinner" --amount 25 --category Food
```

---

### ❌ Delete Expense

```bash
python main.py delete --id 1
```

---

### 📊 View Summary

Total expenses:

```bash
python main.py summary
```

Monthly summary:

```bash
python main.py summary --month 8
```

---

### 💵 Set Budget

```bash
python main.py budget --month 8 --limit 500
```

---

## ⚠️ Notes

* All expenses are stored in `expenses.csv`.
* Budgets are stored in `budget.csv`.
* Dates are automatically assigned when adding an expense.
* Budget warnings are displayed when monthly expenses exceed the set limit.
* Month values must be between 1 and 12.

---

## 🎯 Future Improvements

* Add better error handling for missing files
* Improve input validation
* Add support for editing dates
* Export reports in different formats
* Improve code structure (reduce global state)

---

## 📄 License

This project is for educational purposes.
