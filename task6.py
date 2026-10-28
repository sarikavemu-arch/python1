
passengers = int(input("Enter number of passengers: "))
distance = float(input("Enter distance in km: "))
travel_class = input("Enter class (Sleeper/AC): ").lower()
cancel = input("Cancel ticket? (yes/no): ").lower()

if passengers <= 0 or distance <= 0:
    print("Invalid input")
elif travel_class not in ["sleeper", "ac"]:
    print("Invalid travel class")
elif cancel not in ["yes", "no"]:
    print("Invalid cancellation choice")
else:
    rate = 1 if travel_class == "sleeper" else 2
    fare = distance * rate
    total = 0
    valid = True

    for i in range(passengers):
        age = int(input("Enter passenger age: "))

        if age < 0:
            valid = False
            break

        if age < 5:
            concession = fare
        elif age >= 60:
            concession = fare * 0.20
        else:
            concession = 0

        total += fare - concession + 30

    if not valid:
        print("Invalid passenger age")
    else:
        print("Total reservation fare:", total)

        if cancel == "yes":
            penalty = total * 0.25
            print("Cancellation penalty:", penalty)
            print("Refund:", total - penalty)
        else:
            print("Ticket confirmed")

