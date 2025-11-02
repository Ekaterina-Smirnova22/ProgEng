class Animal:
    def __init__(self, name, klass):
        self.name = name
        self.klass = klass

    def place(self):
        living_environment = input(f'Введите, где обитает {self.name}:')
        print(f"Верно,", living_environment, " - среда обитания таких животных как", {self.name} )

class Pet(Animal):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def wild(self):
        pett = input('Это дикое или домашнее животное?')
        if pett == 'дикое':
            print(f'{self.type}  {self.name} живет в зоопарке')
        else:
            print(f'Ваше домашнее животное - {self.type}, кличка {self.name}')

pet = Pet("Анфиса", "кошка")
pet.place()
pet.wild()
