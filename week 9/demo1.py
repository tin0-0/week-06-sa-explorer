class Transaction:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def vat(self):
        return self.amount * 0.15
    
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

thabo = student("Thabo", 19)
paul = student("Paul", 25)

print(thabo.name)
print(thabo.age)
print(f"Name:{paul.name} Age: {paul.age}")

print(id(thabo))
print(id(paul))

print(type(thabo))
print(type("ABC"))