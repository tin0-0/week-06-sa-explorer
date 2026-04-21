#(A) SAMunicipalBill — attributes: account_holder, water_units, electricity_units. Methods: add_water(units), add_electricity(units), total_due(water_rate, elec_rate) returning the calculated amount.
class SA_Municipal_Bill:
    def __init__(self,account_holder, water_units, electricity_units):
        self.account_holder = account_holder
        self.water_units = water_units
        self.electricty_units = electricity_units 
        add_water = 0
        

    def add_water(self, water_units)