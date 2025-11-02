class Car: # создаем класс Car

    def __init__(self, make, model): # создаем метод инициализации, который вызывается при создании нового экземпляра класса
        self.make = make # сохраняем марки автомобиля в атрибуте 'make'
        self.model = model #сохраняем модели автомобиля в атрибуте 'model'

    def drive(self): # создаем метод для вождения автомобиля
        print(f"Driving the {self.make} {self.model}") # выводим информацию о текущем автомобиле

class ElectricCar(Car): # создаем класс ElectricCar, наследующий от класса Car
    def __init__(self, make, model, battery_capacity): # создаем метод инициализации экземпляра класса ElectricCar
        super().__init__(make, model) #вызываем метод инициализации родительского класса Car
        self.battery_capacity = battery_capacity # сохраняем емкости батареи в атрибуте 'battery_capacity'

    def charge(self):# создаем метод зарядки электромобиля
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") # выводим сообщение о зарядке электромобиля

my_electric_car = ElectricCar("Mitsubishi", "Lancer", 100) # Создаем экземпляр класса ElectricCar
my_electric_car.drive() # вызываем метод drive у созданного экземпляра
my_electric_car.charge() # вызываем метод зарядки для созданного экземпляра