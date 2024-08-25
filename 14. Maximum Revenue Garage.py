class Garage:
    def __init__(self, bikes, cars, trucks):
        self.bikes = bikes
        self.cars = cars
        self.trucks = trucks

def MaxRevenue(garages):
    if garages is None:
        return -1
    
    max_revenue = 0
    
    for garage in garages:
        revenue = (100 * garage.bikes) + (250 * garage.cars) + (500 * garage.trucks)
        if revenue > max_revenue:
            max_revenue = revenue
    
    return max_revenue
