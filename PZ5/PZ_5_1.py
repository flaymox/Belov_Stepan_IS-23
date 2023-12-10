# Составить функцию, которая выполнит суммирования числового ряда.
def sum_of_series(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

n = int(input("Введите число:"))
result_sum = sum_of_series(n)
print(f"Сумма числового ряда до {n} равна {result_sum}")