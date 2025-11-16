class InvalidOperationError(Exception): # определение пользовательского исключения для ошибок с операциями суммы
    def __init__(self, message="Недопустимая операция"):
        # конструктор базового класса с сообщением об ошибке
        super().__init__(message)

def sum_numbers(numbers): # функция для суммирования списка чисел с проверкой корректности входных данных
    if not isinstance(numbers, list):
        # ошибка, если передан не список
        raise InvalidOperationError("Входные данные должны быть списком чисел")

    total = 0
    for num in numbers:
        if not isinstance(num, (int, float)):
            # ошибка, если элемент списка не число
            raise InvalidOperationError(f"Элемент '{num}' не является числом")
        total += num

    return total


# функция сложения двух чисел с проверкой типов аргументов
def add_two_values(a, b):
    if not all(isinstance(x, (int, float)) for x in (a, b)):
        # Ошибка, если хотя бы один аргумент не число
        raise InvalidOperationError("Оба аргумента должны быть числами")

    return a + b


#использование первой функции
try:
    print("Сумма списка:", sum_numbers([1, 2, 3, 4]))
    print("Сумма списка:", sum_numbers([1, "2", 3]))
except InvalidOperationError as e:
    print(f"Ошибка: {e}")

#использование второй функции
try:
    print("Сложение двух чисел:", add_two_values(5, 7))
    print("Сложение двух чисел:", add_two_values(5, "семь"))  
except InvalidOperationError as e:
    print(f"Ошибка: {e}")
