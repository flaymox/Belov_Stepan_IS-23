import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('kafedra.db')
cursor = conn.cursor()

# Создаем таблицу Преподавательский состав
cursor.execute('''CREATE TABLE IF NOT EXISTS ПреподавательскийСостав (
                    Табельный_номер INTEGER PRIMARY KEY,
                    Фамилия_И_О TEXT,
                    Дата_рождения TEXT,
                    Должность TEXT,
                    Ученая_Степень TEXT,
                    Нагрузка REAL,
                    Зарплата REAL
                 )''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()