class NoteTwo:
    count = 0

    def __init__(self, content, is_completed=False):
        self.content = content
        self.is_completed = is_completed
        NoteTwo.count += 1

    @classmethod
    def reset_count(cls):
        cls.count = 0


# Создание экземпляра с новым атрибутом
note = NoteTwo("Sample content", is_completed=True)

# Вывод значений собственных атрибутов экземпляра
print(note.__dict__)

# Увеличение счетчика на величину, передаваемую в качестве аргумента
increment_amount = 5
NoteTwo.count += increment_amount

# Проверка содержимого магической переменной __dict__
print(NoteTwo.__dict__)
