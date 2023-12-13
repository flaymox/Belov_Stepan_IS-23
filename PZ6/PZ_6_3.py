# Дан список размера N (N — четное число). Программа меняет местами его первый элемент
# со вторым, третий — с четвертым и т. д.
# Ввод списка размера N (число должно быть четным)
N = int(input("Введите четное число N: "))

if N % 2 == 0:
    # Ввод элементов списка через пробел
    my_list = list(map(int, input("Введите элементы списка через пробел: ").split()))
    
    if len(my_list) == N:
        print("Исходный список:", my_list)

        # Смена мест соседних элементов
        for i in range(0, len(my_list), 2):
            if i + 1 < len(my_list):
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

        print("Измененный список:", my_list)
    else:
        print("Количество элементов списка не соответствует введенному размеру N.")
else:
    print("Введите четное число для размера списка.")
