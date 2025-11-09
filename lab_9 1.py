class Ekaterina:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Екатерина':
            self.name = f"Все верно, я {name}"
        else:
            self.name = f"Неправильно, я не {name} , а Екатерина"

person1 = Ekaterina ('Виктория')
person2 = Ekaterina ('Екатерина')
print(person1.name)
print(person2.name)

person.surname = 'Смирнова'