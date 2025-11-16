def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().strip()
            if not data:
                raise ValueError("Файл пустой")
            return data
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(e)

print("Проверка pysto.txt:")
result = read_file('pysto.txt')
if result is not None:
    print(result)

print("\nПроверка ne_pysto.txt:")
result = read_file('ne_pysto.txt')
if result is not None:
    print(result)