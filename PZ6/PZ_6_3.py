def swap_elements(lst):
    # Проверка на четность длины списка
    if len(lst) % 2 != 0:
        print("Ошибка: Длина списка должна быть четным числом.")
        return

    # Обмен элементов
    for i in range(0, len(lst), 2):
        # Используем временную переменную для обмена значениями
        temp = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = temp

    return lst

# Пример использования
if __name__ == "__main__":
    # Задайте свой список
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]

    # Вызов функции для обмена элементов
    result_list = swap_elements(my_list)

    # Вывод результата
    print("Исходный список:", my_list)
    print("Список после обмена элементов:", result_list)
