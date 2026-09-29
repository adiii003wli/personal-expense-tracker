print("Personal Expense Tracker")
print("------------------------")

income = float(input("Enter your monthly income: ₹"))
expense = float(input("Enter your total expenses: ₹"))

balance = income - expense

print("\n----- Summary -----")
print("Income: ₹", income)
print("Expenses: ₹", expense)
print("Remaining Balance: ₹", balance)

if balance > 0:
    print("You are within your income.")
elif balance == 0:
    print("Your income and expenses are equal.")
else:
    print("You spent more than your income.")