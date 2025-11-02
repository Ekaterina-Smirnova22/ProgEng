class Animal:
    def __init__(self, name, klass):
        self.name = name
        self.klass = klass

animal = Animal("морской котик", "млекопитающие")
print(f'Животное {animal.name} принадлежит классу {animal.klass}')