# Вывод путь S, пройденный лодкой по озеру и реке (против течения).

V = float(input("Введите скорость лодки в стоячей воде (км/ч): "))
U = float(input("Введите скорость течения реки км/ч: "))
if U < V: # Обработка исключений.
    T1 = float(input("Введите время движения лодки по озеру (часы): "))
    T2 = float(input("Введите время движения лодки по реке против течения (часы): "))
    S1 = V * T1 # Нахождение время движения лодки по озеру.
    S2 = (V - U) * T2 # Нахождение время движения лодки по реке (против течения).
    S = S1 + S2 # Нахождение общего пройденного пути.
    print(f"Путь, пройденный лодкой, составляет {S} км.")
else:
    print("Ошибка: Скорость течения реки должна быть меньше скорости лодки в стоячей воде.")