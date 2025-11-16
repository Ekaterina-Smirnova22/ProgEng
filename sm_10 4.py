class CallCounter:
    def __init__(self):
        self.count = 0  # инициализация счётчика вызовов функции

    def __call__(self, func):
        """
        Метод __call__ позволяет объекту класса Trace вести себя как функция.
        Он принимает функцию f и возвращает обёртку для этой функции.
        """
        def wrapper(*args, **kwargs): #срабатывает при вызове функции
            self.count += 1  # увеличение счётчика вызовов
            print(f"Функция '{func.__name__}' вызвана {self.count} раз(а)")
            return func(*args, **kwargs)  #вызов оригинальной функции

        return wrapper #возвращает функцию-обёртку вместо оригинальной

#функция приветствия пользователя
@CallCounter()  # приминение декоратора - оборачивая greet
def greet(name):
    return f"Привет, {name}!"

#функция подсчёта суммы списка чисел
@CallCounter()  #приминение декоратора - оборачиваем sum_list
def sum_list(numbers):
    return sum(numbers)

#вызовы функций, демонстрирующие работу декоратора
print(greet("Катя")) #первый вызов greet, счётчик = 1
print(greet("Саша")) #второй вызов greet, счётчик = 2

print(sum_list([1, 2, 3])) # первый вызов sum_list, счётчик = 1
print(sum_list([10, 20])) # второй вызов sum_list, счётчик = 2
print(sum_list([7, 8, 9, 10])) # третий вызов sum_list, счётчик = 3
