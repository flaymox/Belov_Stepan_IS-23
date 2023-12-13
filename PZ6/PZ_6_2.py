my_list = [5, 6, 8, 6, 7]

n = len(my_list)

if n < 3:
    print("Невозможно найти локальный минимум.")
else:
    for i in range(1, n - 1):
        if my_list[i - 1] > my_list[i] < my_list[i + 1]:
            print(f"Найден локальный минимум в индексе {i}")
            break
    else:
        print("Локальный минимум не найден.")
