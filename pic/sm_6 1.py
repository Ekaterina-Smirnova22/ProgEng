marial = input ('Ведите числа через пробел: ')

numbers_list = list(map(int, marial.split()))
numbers_tuple = tuple(numbers_list)

print('Список: ', numbers_list)
print('Кортеж: ', numbers_tuple)