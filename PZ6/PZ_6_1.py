# Вводим первый член и разность
A = float(input("Введите первый член (A) арифметической прогрессии: "))
D = float(input("Введите разность (D) арифметической прогрессии: "))

# Задаем размер прогрессии
n = 10

# Формируем и выводим список
progression = [A + i * D for i in range(n)]
print("Арифметическая прогрессия:", progression)
