class Animal:
    def name_of_animal(self):
        pass
    def color(self):
        pass

class Fish(Animal):
    def __init__(self, name):
        self.name = name
    def name_of_animal(self):
        return self.name
    def color(self):
        print('серебристый')

class Bird(Animal):
    def __init__(self, name):
        self.name = name
    def name_of_animal(self):
        return self.name
    def color(self):
        print('красный')

animals = [Fish('Булька'), Bird('Чирик')]

for animal in animals:
    print(f"Имя животного: {animal.name_of_animal()}")
    animal.color()