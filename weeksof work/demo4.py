import random

print(random.randint(1, 10))

print(random.choice(["heads", "tails"]))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

print(random.sample(range(1, 53), 6))

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
picked = random.choice(students)
print(f"Today's answer comes from: {picked}")

flip = random.choice(["heads", "tails"])
print(f"The coin flip result is: {flip}")



die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
if die1 == die2:
    double = True 
else:
    double = False



print(f"You rolled a {die1} and a {die2}, for a total of {die1 + die2}.")

provinces = ["Gauteng", "KwaZulu-Natal", "Western Cape", "Eastern Cape", "Limpopo", "Mpumalanga", "North West", "Free State", "Northern Cape"]
question_province = random.choice(provinces)
print(f"Which province is the capital of South Africa located in? {question_province}")


random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))

random.seed(42)
print(random.randint(1, 100))
print(random.randint(1, 100))

print(random.sample(range(1, 53), 6))