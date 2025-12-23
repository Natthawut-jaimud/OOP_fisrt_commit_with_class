class Car:
    def __init__(self, Model, Brand):
        self.Model = Model
        self.Brand = Brand
    def drive(self):
        print(f"{self.Brand}, {self.Model} is drivring")


class ElectricCar(Car):
    def __init__(self,Model, Brand,battery_size):
        super().__init__(Model, Brand)
        self.battery_size = battery_size
    
    def charge(self):
        print(f"Battery is charging {self.battery_size}")


my_car = Car("Toyota", "vios")
my_car.drive()

ev_car1 = ElectricCar("Toyota", "vios",1000)
ev_car1.charge()
