#naming error
student_name = "paul"
print(student_name)

income = 300000
if income <= 237100:
    tax = income * 0.18
elif income <= 370500:
    tax = 42678 + (income - 237100) * 0.26
print (f"Tax: R{tax:.2f}")
