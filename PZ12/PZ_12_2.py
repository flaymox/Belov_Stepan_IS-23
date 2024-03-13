string = "abc123def456ghi789"
digits_generator = (int(char) for char in string if char.isdigit())
print(list(digits_generator))  # Выведет: [1, 2, 3, 4, 5, 6, 7, 8, 9]
