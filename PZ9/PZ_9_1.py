data = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
items = data.split()

sales_data = {items[i]: max(map(int, items[i + 1:i + 6])) for i in range(0, len(items), 6)}

for product, max_sales in sales_data.items():
    print(f"Максимальные продажи для {product}: {max_sales}")
