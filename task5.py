

usage = float(input("Enter data usage in GB: "))
days = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget: "))

plans = [
    ["Plan A", 199, 20, 28, 10],
    ["Plan B", 299, 40, 56, 8],
    ["Plan C", 399, 80, 84, 5]
]

best_plan = ""
best_cost = float("inf")

if usage < 0 or days <= 0 or budget < 0:
    print("Invalid input")
else:
    for plan in plans:
        name, price, data, validity, extra_rate = plan
        extra = max(0, usage - data)
        total = price + extra * extra_rate

        if validity >= days and total <= budget:
            if total < best_cost:
                best_cost = total
                best_plan = name

    if best_plan:
        print("Most economical plan:", best_plan)
        print("Total cost:", best_cost)
    else:
        print("No eligible plan found")

