class vehicle:
    def __init__(self,registration,make,model,): # type: ignore
        self.registration = registration
        self.make = make
        self.model = model
          
        
    def describe(self):
        return f"{self.make} {self.model} ({self.registration})"
    
class Car(vehicle):
    def __init__(self,registration,make,model, num_seats):
        super().__init__(registration,make,model)
        self.num_seats = num_seats

class truck(vehicle):
    def __init__(self,registration,make,model, num_seats,load_weight):
        super().__init__(registration,make,model)
        self.num_seats = num_seats
        self.load_weight = load_weight

    def describe(self):
        base = super().describe()
        return f"{base} - {self.num_seats} seats - {self.load_weight}Kg"
    
# my_car = Car("HK08PGGP", "Toyota", "Corolla", 5)
# print(my_car.describe())

# my_truck = truck("KH06GWGP", "Volvo", "serious", 2 ,1500)
# print(my_truck.describe())

fleet = [
    Car("CA 111", "Toyota", "Corolla", 5), truck("GP 333", "Isuzu", "NPR", 2,3500)
]

for vehicle in fleet:
    print(vehicle.describe())