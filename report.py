def category_summary(expenses):
    summary = {}
    for item in expenses:
        category = item["category"]
        summary[category] = summary.get(category, 0) + item["amount"]

    print("Category Summary:")
    for key, value in summary.items():
        print(key, value)