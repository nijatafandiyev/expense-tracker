

Features: add expenses, list them, see totals per category.
Data is saved to expenses.json so it is kept between runs.
"""

import json
from datetime import date

FILE_NAME = "expenses.json"


def load_expenses():
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
   
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)


def add_expense(expenses):
   
    category = input("Category (e.g. food, transport): ").strip().lower()
    try:
        amount = float(input("Amount (HUF): "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expenses.append({
        "date": str(date.today()),
        "category": category,
        "amount": amount,
    })
    save_expenses(expenses)
    print("Expense added.")


def list_expenses(expenses):
    """Print all expenses."""
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['date']} | {e['category']:<12} | {e['amount']:.0f} HUF")


def show_summary(expenses):
   
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    for category, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{category:<12} {total:.0f} HUF")
    print(f"{'TOTAL':<12} {sum(totals.values()):.0f} HUF")


def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Summary by category")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
