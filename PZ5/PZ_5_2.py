import math
# Вычисляет периметр и площадь равностороннего треугольника.
def TrianglePS(a):
    while a > 0:
        perimeter = 3 * a
        area = (a**2) * math.sqrt(3) / 4
        return perimeter, area
    else:
        print("Ошибка ввода!")
        return None

# Ввод стороны для треугольника 1
side1 = float(input("Введите сторону треугольника 1: "))
perimeter1, area1 = TrianglePS(side1)
print("Треугольник 1:")
print(f"Сторона треугольника: {side1}")
print(f"Периметр треугольника: {perimeter1}")
print(f"Площадь треугольника: {area1}")

# Ввод стороны для треугольника 2
side2 = float(input("Введите сторону треугольника 2: "))
perimeter2, area2 = TrianglePS(side2)
print("Треугольник 2:")
print(f"Сторона треугольника: {side2}")
print(f"Периметр треугольника: {perimeter2}")
print(f"Площадь треугольника: {area2}")

# Ввод стороны для треугольника 3
side3 = float(input("Введите сторону треугольника 3: "))
perimeter3, area3 = TrianglePS(side3)
print("Треугольник 3:")
print(f"Сторона треугольника: {side3}")
print(f"Периметр треугольника: {perimeter3}")
print(f"Площадь треугольника: {area3}")
