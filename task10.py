
students = int(input("Enter number of ticket buyers: "))
ticket_price = float(input("Enter ticket price: "))
sponsorship = float(input("Enter sponsorship amount: "))
venue = float(input("Enter venue cost: "))
food = float(input("Enter food cost: "))
decoration = float(input("Enter decoration cost: "))
other = float(input("Enter other expenses: "))
target = float(input("Enter target profit: "))

if (min(ticket_price, sponsorship, venue, food,
        decoration, other, target) < 0 or students < 0):
    print("Invalid input")
else:
    ticket_income = students * ticket_price
    total_income = ticket_income + sponsorship
    total_expense = venue + food + decoration + other
    profit = total_income - total_expense

    print("Ticket income:", ticket_income)
    print("Total income:", total_income)
    print("Total expenses:", total_expense)
    print("Event profit:", profit)

    if profit >= target:
        print("Event budget successful")
    else:
        print("Event profit target not achieved")

    if profit < 0:
        print("Event resulted in a loss")
