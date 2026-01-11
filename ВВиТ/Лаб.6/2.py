class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
        def __init__(self, make, model, fuel_type):
            super().__init__(make, model)
            self.fuel_type = fuel_type

        def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, Тип топлива: {self.fuel_type}"


vehicle = Vehicle("Porsche 911", "911 Turbo серии 997")

car1 = Car("Toyota", "Camry", "бензин")
car2 = Car("Tesla", "Model S", "электричество")
car3 = Car("Volkswagen", "Golf", "дизель")

print("Базовый класс Vehicle:")
print(vehicle.get_info())
print(car1.get_info())