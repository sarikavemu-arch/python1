
consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))

if min(consultation, diagnostic, treatment) < 0:
    print("Invalid charges")
else:
    total = consultation + diagnostic + treatment

    if total >= 5000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    if final_bill >= 5000:
        category = "High payment"
    elif final_bill >= 2000:
        category = "Medium payment"
    else:
        category = "Low payment"

    print("Total charges:", total)
    print("Concession:", concession)
    print("Final bill:", final_bill)
    print("Patient category:", category)

