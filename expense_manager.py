def add_expense(expenses, amount, category):
    expenses.append({
        "amount": amount,
        "category": category
    })
    print("Expense added")


def view_total(expenses):
    total = sum(item["amount"] for item in expenses)
    print("Total Expense:", total)