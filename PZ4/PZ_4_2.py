# Программа которая выводит есть ли в числе цифра 2
number = int(input("Введите целое число N: "))
has_digit_two = False # присваивание начального значения
while number > 0: # цикл с условием
    if number % 10 == 2: #
        has_digit_two = True
        break
    number = number // 10
print(has_digit_two)