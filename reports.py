def generate_summary(expenses):
    if not expenses:
        return "No data available."

    total = sum(float(e['amount']) for e in expenses)
    avg = total / len(expenses)
    
    categories = {}
    for e in expenses:
        cat = e['category']
        categories[cat] = categories.get(cat, 0) + float(e['amount'])

    report = f"\n--- Financial Report ---\n"
    report += f"Total Spending: ${total:.2f}\n"
    report += f"Average Expense: ${avg:.2f}\n"
    report += "Category Breakdown:\n"
    for cat, amt in categories.items():
        report += f" - {cat}: ${amt:.2f}\n"
    
    return report

def generate_category_chart(expenses):
    if not expenses:
        return "No data available for chart."

    categories = {}
    total_spending = 0.0
    for e in expenses:
        amount = float(e['amount'])
        cat = e['category']
        categories[cat] = categories.get(cat, 0) + amount
        total_spending += amount

    if total_spending == 0:
        return "No spending to chart."

    chart = "\n--- Spending Chart by Category ---\n"
    max_bar_width = 50
    for category, amount in sorted(categories.items(), key=lambda item: item[1], reverse=True):
        percentage = amount / total_spending
        bar_width = int(percentage * max_bar_width)
        bar = "█" * bar_width
        chart += f"{category:<15} | {bar} {percentage:.1%}\n"
    
    return chart

def get_summary_data(expenses):
    if not expenses:
        return {"total": 0.0, "average": 0.0, "categories": {}}

    total = sum(float(e['amount']) for e in expenses)
    avg = total / len(expenses)
    
    categories = {}
    for e in expenses:
        cat = e['category']
        categories[cat] = categories.get(cat, 0) + float(e['amount'])
        
    return {"total": total, "average": avg, "categories": categories}