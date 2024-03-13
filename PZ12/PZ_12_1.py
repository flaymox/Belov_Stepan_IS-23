# Организовать и вывести последовательность из N случайных целых чисел. Из
# исходной последовательности организовать первую последовательность, содержащую
# числа кратные трем, и вторую – для всех остальных. Найти количество элементов в
# полученных последовательностях.

import random

# Ввод числа N
N = int(input("Введите количество чисел в последовательности: "))

# Генерация случайной последовательности из N чисел
random_sequence = [random.randint(1, 100) for _ in range(N)]

# Разделение последовательности на числа кратные трем и не кратные трем
divisible_by_three = [num for num in random_sequence if num % 3 == 0]
not_divisible_by_three = [num for num in random_sequence if num % 3 != 0]

# Подсчет количества элементов в каждой последовательности
count_divisible_by_three = sum(1 for _ in divisible_by_three)
count_not_divisible_by_three = sum(1 for _ in not_divisible_by_three)

# Вывод результатов
print("Случайная последовательность:", random_sequence)
print("Числа кратные трем:", divisible_by_three)
print("Числа не кратные трем:", not_divisible_by_three)
print("Количество элементов в последовательности кратных трем:", count_divisible_by_three)
print("Количество элементов в последовательности не кратных трем:", count_not_divisible_by_three)
