string = input("Введите строку: ")
digits_generator = (int(char) for char in string if char.isdigit())
print(list(digits_generator))
