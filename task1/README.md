
# University Scholarship Allocation

name = input("Enter student name: ")
marks = float(input("Enter aggregate marks: "))
subject1 = float(input("Enter subject 1 marks: "))
subject2 = float(input("Enter subject 2 marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if (marks >= 75 and subject1 >= 40 and subject2 >= 40
        and attendance >= 75 and income <= 200000):
    print("\nScholarship Status: Eligible")
else:
    print("\nScholarship Status: Not Eligible")

Algorithm
1. Start.
2. Read the student's name, aggregate marks, subject marks, attendance, and annual family income.
3. Check whether aggregate marks are at least 75.
4. Check whether both subject marks are at least 40.
5. Check whether attendance is at least 75% and annual family income is at most ₹2,00,000.
6. If all conditions are satisfied, display “Eligible”; otherwise, display “Not Eligible”.
7. Stop.
8. pseudocode
9.  START
INPUT mobile usage details
INPUT budget and validity
INPUT available mobile plans

FOR each mobile plan
    CALCULATE total plan cost
    CHECK data and call usage
    CALCULATE excess charges
    CHECK budget and validity

    IF plan satisfies all conditions
        MARK plan as eligible
    END IF
END FOR

SELECT the lowest-cost eligible plan

DISPLAY eligible plans
DISPLAY most economical plan
STOP
   ```mermaid
   flowchart TD
    A([START]) --> B[/Input marks, subject marks, attendance, income/]
    B --> C{Aggregate marks >= 75?}
    C -- No --> H[/Display Not Eligible/]
    C -- Yes --> D{Both subject marks >= 40?}
    D -- No --> H
    D -- Yes --> E{Attendance >= 75%?}
    E -- No --> H
    E -- Yes --> F{Annual income <= 200000?}
    F -- No --> H
    F -- Yes --> G[/Display Eligible/]
    G --> I([STOP])
    H --> I
    classDef bw fill:#ffffff,color:#000000,stroke:#000000,stroke-width:1px;
    class A,B,C,D,E,F,G,H,I bw;
   ```
Example and Sample Output
Input:

Enter student name: Ravi
Enter aggregate marks: 85
Enter subject 1 marks: 80
Enter subject 2 marks: 75
Enter attendance percentage: 90
Enter annual family income: 150000
Output
Scholarship Status: Eligible

Test Cases
Test Case	Input	Expected Output
1	Usage within plan	No excess charges
2	Usage exceeds data limit	Extra charges applied
3	Cost within budget	Plan eligible
4	Cost exceeds budget	Plan not eligible

Conclusion
The program compares multiple mobile plans based on usage, validity, and budget. It calculates extra charges and identifies the most economical eligible plan.
