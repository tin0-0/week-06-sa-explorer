class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} says meow!"   
#test
rex = Dog("Rex", "Jack Russell")
print(rex.name)
print(rex.breed)
print(rex.speak())

print()

leaf = Cat("leaf", "Ginger")
print(leaf.name)
print(leaf.breed)
print(leaf.speak())