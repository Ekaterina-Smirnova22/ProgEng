def count_grades():
    while True:
        s = input("Введите оценки через пробел: ").strip()
        if not s:
            print("Вы не ввели оценки. Попробуйте ещё раз.")
            continue
        parts = s.split()
        try:
            grades = tuple(int(x) for x in parts)
        except ValueError:
            print("Ошибка: нужно вводить только числа, например: 2 3 4 5.")
            continue
        if any(g < 2 or g > 5 for g in grades):
            print("Ошибка: оценки должны быть числами от 2 до 5.")
            continue
        break

    print(grades)
    for g in range(2, 6):
        print(f"оценка : {g} количество: {grades.count(g)}")

if __name__ == "__main__":
    count_grades()