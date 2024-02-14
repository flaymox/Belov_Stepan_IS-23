# Задача 1: Обработка чисел
with open('input_numbers.txt', 'r') as f:
    lines = f.readlines()

numbers = [int(num) for num in lines[0].split()]
num_count = len(numbers)
min_num = min(numbers)
even_squares = [num**2 for num in numbers if num % 2 == 0]
sum_even_squares = sum(even_squares)
avg_even_squares = sum_even_squares / len(even_squares) if even_squares else 0

# Запись результатов в новый файл
with open('output_numbers.txt', 'w') as f:
    f.write('Исходные данные:\n')
    f.write(f'Количество элементов: {num_count}\n')
    f.write(f'Минимальный элемент: {min_num}\n')
    f.write(f'Квадраты четных элементов: {even_squares}\n')
    f.write(f'Сумма квадратов четных элементов: {sum_even_squares}\n')
    f.write(f'Среднее арифметическое суммы квадратов четных элементов: {avg_even_squares}\n')
