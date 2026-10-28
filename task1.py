
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
