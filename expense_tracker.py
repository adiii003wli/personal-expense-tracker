
print("=" * 35)
print("      PERSONAL EXPENSE TRACKER")
print("=" * 35)

# Get income and budget
income = float(input("Enter your monthly income: ₹"))
budget = float(input("Enter your monthly budget: ₹"))

print("\nEnter your expenses:")

# Expense categories
food = float(input("Food: ₹"))
travel = float(input("Travel: ₹"))
shopping = float(input("Shopping: ₹"))
bills = float(input("Bills: ₹"))
other = float(input("Other: ₹"))

# Calculate total expenses
total_expenses = food + travel + shopping + bills + other

# Calculate balances
remaining_income = income - total_expenses
remaining_budget = budget - total_expenses

# Display summary
print("\n" + "=" * 35)
print("           EXPENSE SUMMARY")
print("=" * 35)

print(f"Income: ₹{income:.2f}")
print(f"Budget: ₹{budget:.2f}")

print("\nExpenses:")
print(f"Food: ₹{food:.2f}")
print(f"Travel: ₹{travel:.2f}")
print(f"Shopping: ₹{shopping:.2f}")
print(f"Bills: ₹{bills:.2f}")
print(f"Other: ₹{other:.2f}")

print(f"\nTotal Expenses: ₹{total_expenses:.2f}")
print(f"Remaining Income: ₹{remaining_income:.2f}")
print(f"Remaining Budget: ₹{remaining_budget:.2f}")

# Budget status
print("\nBudget Status:")

if remaining_budget > 0:
    print(f"You are within your budget by ₹{remaining_budget:.2f}")
elif remaining_budget == 0:
    print("You have exactly reached your budget.")
else:
    print(f"You exceeded your budget by ₹{abs(remaining_budget):.2f}")

# Income status
print("\nIncome Status:")

if remaining_income > 0:
    print("You have money remaining after expenses.")
elif remaining_income == 0:
    print("Your expenses equal your income.")
else:
    print(f"You spent ₹{abs(remaining_income):.2f} more than your income.")

print("\n" + "=" * 35)
print("       TRACKING COMPLETE")
print("=" * 35)