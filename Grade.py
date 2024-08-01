def assign_grade(percentage):
    if percentage>=90:
        return "Grade A"
    elif percentage>=80:
        return "Grade B"
    elif percentage>=70:
        return "Grade C"
    elif percentage>=60:
        return "Grade D"
    elif percentage>=40:
        return "Grade E"
    else:
        return "Grade F"
percentage=float(input("Enter the percentage:"))
grade=assign_grade(percentage)
print("The grade of the percentage is",grade)
