def arithmetic_progression(a, d, n):
    """
    Функция для создания арифметической прогрессии.

    :param a: Первый член прогрессии
    :param d: Разность прогрессии
    :param n: Количество членов прогрессии
    :return: Список, содержащий первые n членов арифметической прогрессии
    """
    progression_list = [a + i * d for i in range(n)]
    return progression_list

# Введите первый член и разность
first_term = float(input("Введите первый член арифметической прогрессии (A): "))
difference = float(input("Введите разность арифметической прогрессии (D): "))

# Создайте и выведите список первых 10 членов прогрессии
progression = arithmetic_progression(first_term, difference, 10)
print("Первые 10 членов арифметической прогрессии:", progression)
