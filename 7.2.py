import sqlite3

conn = sqlite3.connect('lab7.db')
cursor = conn.cursor()

# Обновляем оценку студента с id = 3 (Пётр Сидоров)
cursor.execute('UPDATE students SET grade = ? WHERE id = ?', (4.0, 3))
conn.commit()

print("Запись обновлена.")

# Проверим результат
cursor.execute('SELECT * FROM students WHERE id = 3')
row = cursor.fetchone()
print("Обновлённая запись:", row)

conn.close()