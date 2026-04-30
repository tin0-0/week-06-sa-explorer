with open("names.csv", "r") as f:
    header = f.readline().strip().split(",")
    print(header)
    for line in f:
        data = line.strip().split(",")
        print(data)
        surname = data[0]
        name = data[1]
        gender = data[2]
        print(f"Name: {name}, Surname: {surname}, Gender: {gender}")

        if gender == "male":
            title = "Mr."
        elif gender == "female":
            title = "Ms."
        else:
            title = ""
        print(f"{title} {name[1].upper()} {surname.upper()}")