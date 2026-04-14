import math

print(math.factorial(6))

# print(math.gcd(12, 18))

# print(math.log(100, 10))

# print(math.degrees(math.pi))
#compound interest calculation
principal = 1000000
rate = 0.1025
years = 5

amount = principal * math.pow(1 + rate, years)

print(f"R{principal:,} at {rate*100:.2f}% for {years} years will grow to R{amount:,.2f}.")

#area
radius = 25
area = math.pi * math.pow(radius,2)
print(f"Area of a {radius}km radius patrol zone: {area:,.0f} km2")

print(math.ceil(237.50 / 50))

