number = int(input("Введите целое число N: "))
has_digit_two = False
while number > 0:
    if number % 10 == 2:
        has_digit_two = True
        break
    number = number // 10
print(has_digit_two)