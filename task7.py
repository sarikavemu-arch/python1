
n = int(input("Enter number of products: "))
subtotal = 0
tax_total = 0

if n <= 0:
    print("Invalid number of products")
else:
    for i in range(n):
        print("Product", i + 1)
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        category = input("Enter category (food/other): ").lower()

        if price < 0 or quantity <= 0:
            print("Invalid product details")
            continue

        amount = price * quantity

        if category == "food":
            tax = amount * 0.05
        else:
            tax = amount * 0.12

        subtotal += amount
        tax_total += tax

        print(name, "Amount:", amount, "Tax:", tax)

    discount = min(subtotal * 0.10, 500) if subtotal >= 2000 else 0
    total = subtotal + tax_total - discount

    print("Subtotal:", subtotal)
    print("Total tax:", tax_total)
    print("Discount:", discount)
    print("Final invoice:", total)

