squares = []# Create an empty list to store the squares
for n in range(1,6):# Loop through numbers 1 to 5
    squares.append(n**2)# Calculate the square of n and add it to the list
print(squares)

squares = [n**2 for n in range(1,6)]# Create a list of squares using list comprehension
print(squares)

scores =[85,42,91,38,77,55]
passed = [s for s in scores if s >= 50]# Create a list of scores that are greater than or equal to 50 using list comprehension
print("Passed:")
print(passed)

numbers = [1,2,3,4,5]
results = [n for n in numbers if n % 2 == 0]# Create a list of even numbers from the original list using list comprehension
print("Even numbers:")
print(results)