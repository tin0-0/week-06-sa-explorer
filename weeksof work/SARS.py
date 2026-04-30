#ask for annual income
#Determine which bracket the income falls into
#Calculate tax using that bracket formula
#Calculate effective rate: tax / income * 100
#Display income, tax, and effective rate
Annual_income = float(input("Enter your annual income: "))
tax = 0
if Annual_income <= 237100:
    tax = Annual_income * 0.18
elif Annual_income <= 370500:
    taxable_income = Annual_income - 237100
    tax = (taxable_income * 0.26) + 42678
 elif Annual_income <