price_per_kg = float(input("Введите цену 1 кг конфет: "))
if price_per_kg > 0:
    for kg in range(1,11):
        price = kg * price_per_kg
        print(f"{kg} кг конфет стоят {price} рублей")
else:
    print("Ошибка в вводе!")