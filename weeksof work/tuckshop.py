#cheese
#milk
#bread
#how much does each item cost?
cheese_cost = 10
milk_cost = 5
bread_cost = 15

#how many of each item do you want to buy?
cheese = int(input("how many blocks of cheese do you want to buy? "))
milk = int(input("how many cartons of milk do you want to buy? "))
bread = int(input("how many loaves of bread do you want to buy? "))

#calculate the total cost of the items
sub_total = (cheese_cost * cheese) + (milk_cost * milk) + (bread_cost * bread)
tax = 0.15
total = ((sub_total * tax) + sub_total)
print(f"cheese: {cheese}")
print(f"milk: {milk}")
print(f"bread: {bread}")
print()
print(f"sub total: R{sub_total:.2f}")
print(f"tax: R{tax:.2f}")
print(f"total: R{total:.2f}")
print()
print("have a lekker day ekse!")