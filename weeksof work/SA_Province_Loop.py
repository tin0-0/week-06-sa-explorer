provinces = ("gauteng", "western cape", "kwazulu-natal", "eastern cape", "free state", "limpopo", "mpumalanga", "northern cape", "north west")
for i, province in enumerate(provinces, 1):
    print(f"{i}. {province}")


search = input("Search for a province: ").lower()
for province in provinces:
    if search in province:
        print(f"Found: {province}")

