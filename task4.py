
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentive: "))

if min(basic, allowance, overtime, incentive) < 0:
    print("Invalid salary details")
else:
    gross = basic + allowance + overtime + incentive

    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = 1000 + (gross - 20000) * 0.10
    else:
        deduction = 3000 + (gross - 40000) * 0.15

    net = gross - deduction

    print("Gross salary:", gross)
    print("Deduction:", deduction)
    print("Net salary:", net)

