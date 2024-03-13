# Составить генератор (yield), который выводит из строки только цифры.

string = input("Введите строку: ")
digits_generator = (int(char) for char in string if char.isdigit())
print(list(digits_generator))
