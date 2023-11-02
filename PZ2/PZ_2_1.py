# Выводит путь S, пройденный лодкой по озеру и реке (против течения).

V = float(input("Введите скорость лодки в стоячей воде (км/ч): "))
U = float(input("Введите скорость течения реки км/ч: "))
if (U < V) and (V > 0) and (U > 0): # Обработка исключений.
    T1 = float(input("Введите время движения лодки по озеру (часы): "))
    T2 = float(input("Введите время движения лодки по реке против течения (часы): "))
    if (T1 > 0) and (T2 >0): # Обработка исключений
        S1 = V * T1 # Нахождение время движения лодки по озеру.
        S2 = (V - U) * T2 # Нахождение время движения лодки по реке (против течения).
        S = S1 + S2 # Нахождение общего пройденного пути.
        print(f"Путь, пройденный лодкой, составляет {S} км.")