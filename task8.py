
material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
quantity = int(input("Enter units produced: "))
price = float(input("Enter selling price per unit: "))
target = float(input("Enter target profit: "))

if min(material, labour, wastage, machine, price, target) < 0 or quantity <= 0:
    print("Invalid input")
else:
    cost = material + labour + wastage + machine
    revenue = quantity * price
    profit = revenue - cost

    print("Total production cost:", cost)
    print("Total revenue:", revenue)
    print("Profit:", profit)

    if profit >= target:
        print("Profit target achieved")
    else:
        print("Profit target not achieved")
