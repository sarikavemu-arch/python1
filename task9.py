
budget = float(input("Enter travel budget in INR: "))
rate = float(input("Enter exchange rate: "))
fee_percent = float(input("Enter conversion fee percentage: "))

if budget < 0 or rate <= 0 or fee_percent < 0:
    print("Invalid input")
else:
    categories = ["Hotel", "Food", "Transport"]
    expenses = []
    total = 0

    for category in categories:
        amount = float(input("Enter " + category + " expense: "))

        if amount < 0:
            print("Invalid expense")
            amount = 0

        inr = amount * rate
        expenses.append(inr)
        total += inr

    fee = total * fee_percent / 100
    final_cost = total + fee

    print("Hotel expense:", expenses[0])
    print("Food expense:", expenses[1])
    print("Transport expense:", expenses[2])
    print("Conversion fee:", fee)
    print("Total travel cost:", final_cost)

    largest = expenses.index(max(expenses))
    print("Largest expense category:", categories[largest])

    if final_cost > budget:
        print("Budget exceeded")
    else:
        print("Within budget")
