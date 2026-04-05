from datetime import datetime


class Expense:
    def __init__(self, id, description, amount, category):
        self.id = id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = datetime.now()
        self.dateString = self.date.strftime("%d/%m/%Y")


def load():
    pass


def addExpense(description, amount, category):
    expenses.append(Expense(currID, description, amount, category))


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
        for expense in expenses:
            sum += expense.amount
        print(f"Total expenses: {sum}")
        return

    summaryMonth = monthsDict[month]
    for expense in expenses:
        sum += expense.amount if expense.date.month == month else 0

    print(f"Total expenses for {summaryMonth}: {sum}")


def getMaxID():
    return 0


expenses = [
    Expense(1, "10 Piece Chicken Fillet", 17, "Food"),
    Expense(2, "Double Cheeseburger", 15, "Food"),
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
getSummary()
