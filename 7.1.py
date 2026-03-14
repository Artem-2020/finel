import sqlite3

# Подключаемся к БД (файл создастся автоматически)
conn = sqlite3.connect('lab7.db')
cursor = conn.cursor()

# Создаём таблицу students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade REAL
    )
''')

# Добавим несколько записей для демонстрации
students_data = [
    ('Иван Петров', 20, 4.5),
    ('Анна Смирнова', 19, 5.0),
    ('Пётр Сидоров', 21, 3.8),
    ('Елена Козлова', 20, 4.2)
]

cursor.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students_data)
conn.commit()

print("База данных создана, таблица students заполнена.")

# Проверим, что записи есть
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
print("Содержимое таблицы:")
for row in rows:
    print(row)

conn.close()