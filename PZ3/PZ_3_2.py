# Разработать программу, выводящую на экран размер скидки на продукты.
purchase_amount = float(input("Введите сумму покупки в рублях: "))
if purchase_amount > 0: # Обработка исключений
        if purchase_amount < 500: # Обработка исключений
                discount = 2
        elif 500 <= purchase_amount < 1000: # Обработка исключений
                discount = 3
        elif 1000 <= purchase_amount < 1500: # Обработка исключений
                discount = 4
        elif 1500 <= purchase_amount < 2000: # Обработка исключений
                discount = 5
        else:
                discount = 0
        print(f"Размер скидки: {discount}%")
else:
        print("Ошибка в вводе!")
