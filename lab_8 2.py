class Car: # создаем класс Car

    def __init__(self, make, model): # создаем метод инициализации, который вызывается при создании нового экземпляра класса
        self.make = make # сохраняем марки автомобиля в атрибуте 'make'
        self.model = model #сохраняем модели автомобиля в атрибуте 'model'

    def drive(self): # создаем метод для вождения автомобиля
        print(f"Driving the {self.make} {self.model}") # выводим информацию о текущем автомобиле

my_car = Car("Mitsubishi", "Lancer") # создание экземпляра класса Car с маркой Mitsubishi и моделью Lancer
my_car.drive() # вызываем метод drive у созданного экземпляра my_car