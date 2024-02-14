# Задача 2: Обработка текстового файла
with open('text18-3.txt', 'r') as f:
    lines = f.readlines()

punctuations_count = 0
for line_num, line in enumerate(lines[:4]):
    punctuations_count += sum(1 for char in line if char in '.,;:?!')

# Запись текста в стихотворной форме в новый файл
with open('output_poem.txt', 'w') as f:
    for i, line in enumerate(lines):
        if i == 2:
            line = ' '.join(str(ord(char)) for char in line)  # Замена символов их числовыми кодами
        f.write(line)

print(f'Количество знаков пунктуации в первых четырёх строках: {punctuations_count}')