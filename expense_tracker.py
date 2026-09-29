print("================================")
print("   PERSONAL EXPENSE TRACKER")
print("================================")

income = float(input("Enter your monthly income: ₹"))
budget = float(input("Enter your monthly budget: ₹"))

print("\nExpense Categories:")
print("1. Food")
print("2. Travel")
print("3. Shopping")
print("4. Bills")
print("5. Other")

food = 0
travel = 0
shopping = 0
bills = 0
other = 0

print("\nEnter expenses for each category.")

food = float(input("Food: ₹"))
travel = float(input("Travel: ₹"))
shopping = float(input("Shopping: ₹"))
bills = float(input("Bills: ₹"))
other = float(input("Other: ₹"))

total_expenses = food + travel + shopping + bills + other
balance = income - total_expenses
budget_balance = budget - total_expenses

print("\n================================")
print("           SUMMARY")
print("================================")

print("Income: ₹", income)
print("Budget: ₹", budget)

print("\nExpenses:")
print("Food: ₹", food)
print("Travel: ₹", travel)
print("Shopping: ₹", shopping)
print("Bills: ₹", bills)
print("Other: ₹", other)

print("\nTotal Expenses: ₹", total_expenses)
print("Remaining Balance: ₹", balance)

if budget_balance > 0:
    print("Budget Remaining: ₹", budget_balance)
elif budget_balance == 0:
    print("You have reached your budget.")
else:
    print("Budget exceeded by: ₹", abs(budget_balance))

print("\n================================")
print("       TRACKING COMPLETE")
print("================================")