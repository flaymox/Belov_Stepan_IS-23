# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин. Определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.

# Начальное множество магазинов и книг
magaziny = {
    "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"},
    "ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
    "БукМаркет": {"Пушкин", "Достоевский", "Маяковский"},
    "Галерея": {"Чехов", "Тютчев", "Пушкин"}
}

# Добавление всех книг в одно множество
all_books = set()
for books in magaziny.values():
    all_books.update(books)

# Нахождение книги которая есть в каждом магазине
common_books = set.intersection(*magaziny.values())

# Нахождение книги которой нет хотя бы в одном магазине
unique_books = set()
for book in all_books:
    found_in = 0
    for store_books in magaziny.values():
        if book in store_books:
            found_in += 1
    if found_in < len(magaziny):
        unique_books.add(book)

# Вывод результатов
print("Полный список всех книг магазинов:")
print(all_books)
print("\nКниги, которые есть во всех магазинах:")
print(common_books)
print("\nХотя бы одна книга, которая есть не во всех магазинах:")
print(unique_books)
