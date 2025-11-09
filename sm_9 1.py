class Tomato:
    # словарь состояний, описывающий этапы созревания
    states = {0: 'Отсутствует', 1: 'Цветение', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index): #инициализация объекта Tomato
        self._index = index #индекс томата для идентификации
        self._state = 0 #текущее состояние томата

    def grow(self): #метод для перехода на следующую стадию
        self._state = self._state + 1

    def is_ripe(self):
        return self._state == 3
    """
    Проверяем, достиг ли томат стадии зрелости.
    Возвращает bool: True, если томат созрел (стадия 3), иначе False.
    """

class TomatoBush: #инициализация объекта TomatoBush
    def __init__(self, tomato_num):
        self.tomatoes = [Tomato(index) for index in range(0, tomato_num)]
    """
    Параметры:
    tomato_num (int): Количество томатов на кусте.
    tomatoes (list): Список объектов Tomato, представляющих томаты на кусте.
    """

    def grow_all(self): #перевод томатов на следующую стадию
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self): #проверка зрелости томатов
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):#удаление всех томатов с куста
        self.tomatoes = []


class Gardener: #инициализация объекта Gardener
    def __init__(self, name, plant):
        self.name = name #имя садовника
        self._plant = plant #куст томатов, за которым ухаживает садовник

    def work(self):
        self._plant.grow_all() #перевод всех томатов с куста на следующую стадию созревания

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Томаты еще не созрели')
        """
        Если все томаты достигли стадии зрелости, урожай собирается,
        и все томаты удаляются с куста. Если не все томаты созрели,
        выводится соответствующее сообщение.
        """

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ")
        print("1. Посадить куст томатов")
        print("2. Назначить садовника на куст")
        print("3. Ухаживать за кустом")
        print("4. Собрать урожай")


Gardener.knowledge_base() # вызов информации о порядке действий для ухода за кустом томатов