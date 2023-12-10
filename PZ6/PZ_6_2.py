def find_local_minimum_index(arr):
    n = len(arr)
    
    # Проверка для списка размера меньше 3
    if n < 3:
        return "Слишком маленький список"

    for i in range(1, n-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            return i  # Нашли локальный минимум, возвращаем его индекс

    return "Локальный минимум не найден"

# Пример использования
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_local_minimum_index(my_list)

print(f"Исходный список: {my_list}")
print(f"Номер первого локального минимума: {result}")
