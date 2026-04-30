months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    rainfall = float(input("Enter the rainfall for " + month + ": "))
    print(f"Rainfall for {month}: {rainfall:.2f} mm")

total_rainfall=0
for month in months:
    total_rainfall=+ rainfall
print(f"Total rainfall: {total_rainfall:.2f} mm")