class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 10

note1 = Note("Задача1")
print(note1)
print(note1.__dict__)
print(dir(note1))
print(note1.txt)

note1.upcount()
print(note1.count)
note1.upcount()
print(note1.count)

print(note1.upcount)
print(Note.upcount)


