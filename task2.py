
units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50
    surcharge = bill * 0.05
    total = bill + fixed_charge + surcharge

    if units < 50:
        total = total - 10

    print("Energy Charge: Rs.", bill)
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", surcharge)
    print("Final Bill: Rs.", round(total, 2))


