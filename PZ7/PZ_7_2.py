# Дана строка, содержащая цифры и строчные латинские буквы. Программа которая, если буквы в строке
# упорядочены по алфавиту, то выводит 0; в противном случае выводит номер первого
# символа строки, нарушающего алфавитный порядок.

# Ввод строки с клавиатуры
input_string = input("Введите строку: ")

# Проверка нарушения алфавитного порядка
for i in range(len(input_string) - 1):
    if input_string[i] > input_string[i + 1]:
        print(f"Нарушение алфавитного порядка на позиции {i + 1}")
        break
else:
    print("0")