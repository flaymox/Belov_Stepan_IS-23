# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.

# Исходная матрица
matrix = [
    [1, 2, 3],
    [4, -5, 6],
    [-7, 8, 9]
]

# Формируем массив из положительных четных элементов
positive_even_numbers = [num for row in matrix for num in row if num > 0 and num % 2 == 0]

# Вычисляем сумму и среднее арифметическое
sum_of_numbers = sum(positive_even_numbers)
average_of_numbers = sum_of_numbers / len(positive_even_numbers) if positive_even_numbers else 0

# Выводим результаты
print("Массив из положительных четных элементов:", positive_even_numbers)
print("Сумма:", sum_of_numbers)
print("Среднее арифметическое:", average_of_numbers)

