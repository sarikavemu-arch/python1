
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

 Algorithm
1. Read passenger count, distance, travel class and cancellation choice.
2. Validate the inputs.
3. Select the fare rate based on travel class.
4. Calculate the base fare.
5. Read each passenger's age and apply the example concession.
6. Add the reservation fee for every passenger.
7. Calculate the total fare.
8. If cancelled, calculate the penalty and refund.
9. Otherwise, confirm the ticket.
10. Stop.

Example and output
Two passengers travel 100 km in Sleeper class. Their ages are 30 and 65.
- First passenger: ₹100 + ₹30 = ₹130.
- Second passenger: ₹100 − ₹20 + ₹30 = ₹110.
- Total fare = ₹240.
            print("Cancellation penalty:", penalty)
            print("Refund:", total - penalty)
        else:
            print("Ticket confirmed")
            Enter number of passengers: 2
Enter distance in km: 100
Enter class (Sleeper/AC): Sleeper
Cancel ticket? (yes/no): no
Enter passenger age: 30
Enter passenger age: 65
Total reservation fare: 240.0
Ticket confirmed
 ```mermaid
flowchart TD
    A([Start]) --> B[/Enter passengers distance class and cancellation choice/]
    B --> C{Inputs valid?}
    C -- No --> D[/Print invalid input/]
    C -- Yes --> E[Set fare rate according to class]
    E --> F[Calculate base fare]
    F --> G[Set passenger counter]
    G --> H[/Enter passenger age/]
    H --> I{Age valid?}
    I -- No --> D
    I -- Yes --> J{Age below 5?}
    J -- Yes --> K[Apply full fare concession]
    J -- No --> L{Age >= 60?}
    L -- Yes --> M[Apply 20 percent concession]
    L -- No --> N[No concession]
    K --> O[Add reservation fee]
    M --> O
    N --> O
    O --> P[Add fare to total]
    P --> Q{More passengers?}
    Q -- Yes --> H
    Q -- No --> R[/Display total fare/]
    R --> S{Cancel ticket?}
    S -- Yes --> T[Calculate penalty and refund]
    S -- No --> U[/Print ticket confirmed/]
    T --> V([End])
    U --> V
    D --> V
```
            
            

