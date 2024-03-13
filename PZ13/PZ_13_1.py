# Пример квадратной матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Увеличиваем элементы на главной диагонали
n = len(matrix)
for i in range(n):
    matrix[i][i] *= 2

# Выводим новую матрицу
for row in matrix:
    print(row)
