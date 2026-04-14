ID_number = (input("Enter the ID number:"))
ID_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#Extracting information from the ID number
year = ID_number[0] + ID_number[1]
month = ID_number[2] + ID_number[3]
day = ID_number[4] + ID_number[5]
print(f"Date of Birth: {day}/{month}/{year}")

gender = int(ID_number[6])
sequence = ID_number[7] + ID_number[8] + ID_number[9]
citizenship = ID_number[10]
legacy =ID_number[11]
checksum = ID_number[12]

#determining the gender
if gender <= 5:
    gender = "Male"
else:
    gender = "Female"
print(f"Gender: {gender}")

if citizenship == "0":
    citizenship = "SA Citizen"
else:    citizenship = "Permanent Resident"
print(f"Citizenship: {citizenship}")