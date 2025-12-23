class Car:
    def __init__(self, Model, Brand):
        self.Model = Model
        self.Brand = Brand
    def drive(self):
        print(f"{self.Brand}, {self.Model} is drivring")


my_car = Car("Toyota","Vios")
my_car.drive()

