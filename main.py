from datetime import datetime


class Expense:
    def __init__(self, id, description, amount, date):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = (datetime.now()).strftime("%Y-%m-%d")


def load():
    pass


def addExpense(description, amount):
    expenses.append(Expense(currID, description, amount))


def deleteExpense(selectedExpense):
    expenses.remove(selectedExpense)


def findExpense(id):
    for expense in expenses:
        if expense.id == id:
            return expense
    raise LookupError("Error: Expense could not be found.")


def viewExpenses():
    print(f"{"ID":<6}{"Description":<48}{"Amount":<14}{"Date":<32}")
    for expense in expenses:
        print(
            f"{expense.id:<6}{expense.description:<48}${expense.amount:<13}{expense.date:<32}"
        )


def getSummary(month=0):
    sum = 0
    if not month:
        for expense in expenses:
            sum += expense.amount
        print(f"Total expenses: {sum}")
        return

    for expense in expenses:
        sum += expense.amount if expense.date.month == summaryMonth else 0
    summaryMonth = monthsDict[month]
    print(f"Total expenses for {summaryMonth}: {sum}")


def getMaxID():
    return 0


expenses = [
    Expense(1, "10 Piece Chicken Fillet", 17, "05/04/2026"),
    Expense(2, "Double Cheeseburger", 17, "11/12/2006"),
]
currID = getMaxID()

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

viewExpenses()
