from datetime import datetime
import csv
import argparse


class Expense:
    def __init__(self, id, description, amount, category, date=datetime.now()):
        self.id = id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date
        self.dateString = self.date.strftime("%d/%m/%Y")


def addExpense(description, amount, category):
    expense = Expense(currID, description, amount, category)
    budgetMonth = expense.date.month
    budget = budgets[budgetMonth]
    if budget == -1:
        expenses.append(expense)
    else:
        expenses.append(Expense(currID, description, amount, category))
        if budget < getSummary(budgetMonth, False):
            print("Warning: Budget Exceeded.")
    exportExpenses()


def deleteExpense(id):
    selectedExpense = findExpense(id)
    expenses.remove(selectedExpense)
    exportExpenses()


def updateExpense(selectedExpense, newDescription, newAmount, newCategory):
    if not newDescription:
        newDescription = selectedExpense.description
    if not newAmount:
        newAmount = selectedExpense.amount
    if not newCategory:
        newCategory = selectedExpense.category
    selectedExpense.description = newDescription
    selectedExpense.amount = newAmount
    selectedExpense.category = newCategory
    exportExpenses()


def findExpense(id):
    id = int(id)
    for expense in expenses:
        if expense.id == id:
            return expense
    raise LookupError("Error: Expense could not be found.")


def viewExpenses(category):
    print(f"{"ID":<6}{"Description":<40}{"Category":<16}{"Amount":<14}{"Date":<10}")
    if not category:
        for expense in expenses:
            print(
                f"{expense.id:<6}{expense.description:<40}{expense.category:<16}${expense.amount:<13}{expense.dateString:<10}"
            )
    else:
        for expense in expenses:
            if expense.category == category:
                print(
                    f"{expense.id:<6}{expense.description:<40}{expense.category:<16}${expense.amount:<13}{expense.dateString:<10}"
                )


def getSummary(month, displayPrintMessage=True):
    sum = 0
    if not month:
        sum = getTotalExpenses()
        print(f"Total expenses: {sum}")
        return

    summaryMonth = monthsDict[month]
    currYear = datetime.now().year
    for expense in expenses:
        sum += (
            expense.amount
            if expense.date.month == month and expense.date.year == currYear
            else 0
        )
    if displayPrintMessage:
        print(f"Total expenses for {summaryMonth} {currYear}: {sum}")
    return sum


def getTotalExpenses():
    sum = 0
    for expense in expenses:
        sum += expense.amount

    return sum


def getNextID():
    maxID = 0
    for expense in expenses:
        if expense.id > maxID:
            maxID = expense.id
    return maxID + 1


def exportExpenses():
    with open("expenses.csv", "w", newline="") as f:
        expenseWriter = csv.writer(f)
        for expense in expenses:
            eID = expense.id
            eDescription = expense.description
            eAmount = expense.amount
            eCategory = expense.category
            eDateString = expense.dateString
            expenseWriter.writerow([eID, eDescription, eAmount, eCategory, eDateString])


def loadExpenses():
    with open("expenses.csv") as f:
        expenseReader = csv.reader(f)
        for row in expenseReader:
            expenses.append(
                Expense(
                    int(row[0]),
                    row[1],
                    int(row[2]),
                    row[3],
                    datetime.strptime(row[4], "%d/%m/%Y"),
                )
            )


def setBudgets(month, budget):
    rows = []
    with open("budget.csv", "r") as f:
        budgetReader = csv.reader(f)
        for row in budgetReader:
            if row[0] == month:
                row[1] = budget
            rows.append(row)

    with open("budget.csv", "w", newline="") as f:
        budgetWriter = csv.writer(f)
        budgetWriter.writerows(rows)


def loadBudgets():
    with open("budget.csv", "r") as f:
        budgetReader = csv.reader(f)
        for row in budgetReader:
            budgets[int(row[0])] = int(row[1])


def loadInfo():
    pass


monthsDict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

budgets = {}
expenses = []

loadExpenses()
loadBudgets()
currID = getNextID()


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command", required=True)

add_parser = subparsers.add_parser("add", help="Add an expense.")
add_parser.add_argument("--description")
add_parser.add_argument("--amount", type=int)
add_parser.add_argument("--category")

update_parser = subparsers.add_parser("update", help="Update an expense.")
update_parser.add_argument("--id")
update_parser.add_argument("--description")
update_parser.add_argument("--amount", type=int)
update_parser.add_argument("--category")

list_parser = subparsers.add_parser("list", help="List all expenses.")
list_parser.add_argument("--category")

summary_parser = subparsers.add_parser("summary", help="Display expenses summary.")
summary_parser.add_argument("--month", type=int)

delete_parser = subparsers.add_parser("delete", help="Delete an expense.")
delete_parser.add_argument("--id", type=int)

budget_parser = subparsers.add_parser("budget", help="Set a budget")
budget_parser.add_argument("--limit")
budget_parser.add_argument("--month")

args = parser.parse_args()

if args.command == "add":
    addExpense(args.description, args.amount, args.category)
    print(f"Expense added successfully (ID: {currID})")
elif args.command == "list":
    viewExpenses(args.category)
elif args.command == "summary":
    getSummary(args.month)
elif args.command == "delete":
    deleteExpense(args.id)
    print("Expense deleted successfully")
elif args.command == "budget":
    setBudgets(args.month, args.limit)
    print("Budgets set successfully")
elif args.command == "update":
    updateExpense(findExpense(args.id), args.description, args.amount, args.category)
    print(f"Expense updated successfully (ID: {args.id})")
