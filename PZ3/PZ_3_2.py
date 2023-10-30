def calculate_discount(purchase_amount):
    if purchase_amount < 500:
        discount = "2%"
    elif 500 <= purchase_amount < 1000:
        discount = "3%"
    elif 1000 <= purchase_amount < 1500:
        discount = "4%"
    elif 1500 <= purchase_amount < 2000:
        discount = "5%"
    else:
        discount = "0%"
    return discount
purchase_amount = float(input("Введите сумму покупки в рублях: "))
discount = calculate_discount(purchase_amount)
print(f"Размер скидки: {discount}")