class Car: # создаем класс Car

    def __init__(self, make, model): # создаем метод инициализации, который вызывается при создании нового экземпляра класса
        self.make = make # сохраняем марки автомобиля в атрибуте 'make'
        self.model = model #сохраняем модели автомобиля в атрибуте 'model'

my_car = Car("Mitsubishi", "Lancer") # создание экземпляра класса Car с маркой Mitsubishi и моделью Lancer
