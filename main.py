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


def load():
    pass


def addExpense(description, amount, category):
    if budget == -1:
        expenses.append(Expense(currID, description, amount, category))
    else:
        expenses.append(Expense(currID, description, amount, category))
        if budget <= getTotalExpenses():
            print("Warning: Budget Exceeded.")


def deleteExpense(selectedExpense):
    expenses.remove(selectedExpense)


def updateExpense(selectedExpense, updatedField, updatedValue):
    if updatedField == "description":
        selectedExpense.description = updatedValue
    elif updatedField == "amount":
        selectedExpense.amount = updatedValue
    elif updatedField == "category":
        selectedExpense.amount = updatedValue
    else:
        raise Exception("Error: Only description or amount can be updated")


def findExpense(id):
    for expense in expenses:
        if expense.id == id:
            return expense
    raise LookupError("Error: Expense could not be found.")


def viewExpenses():
    print(f"{"ID":<6}{"Description":<40}{"Category":<16}{"Amount":<14}{"Date":<10}")
    for expense in expenses:
        print(
            f"{expense.id:<6}{expense.description:<40}{expense.category:<16}${expense.amount:<13}{expense.dateString:<10}"
        )


def getSummary(month=0):
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

    print(f"Total expenses for {summaryMonth} {currYear}: {sum}")


def getTotalExpenses():
    sum = 0
    for expense in expenses:
        sum += expense.amount

    return sum


def getNextID():
    maxID = 1
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


expenses = []
currID = getNextID()

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

budget = 40

# budget = someNum
# exportExpenses()
loadExpenses()
viewExpenses()
getSummary(4)
