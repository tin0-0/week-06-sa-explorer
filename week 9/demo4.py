class vehicle:
    def __init__(self,registration,make,model,year): # type: ignore
        self.registration = registration
        self.make = make
        self.model = model
        self.year = year   
        self.milage = 0
        self.last_service_km = 0
    
    def drive(self,km):
        if km >0:
            self.milage += km

    def service_due(self):
        return self.milage - self.last_service_km >= 15000
            

