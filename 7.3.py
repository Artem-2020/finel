import sqlite3
import csv

conn = sqlite3.connect('lab7.db')
cursor = conn.cursor()

# Получаем все данные из таблицы
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

# Получаем названия столбцов
column_names = [description[0] for description in cursor.description]

# Записываем в CSV-файл
with open('students_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_names)  # заголовок
    writer.writerows(rows)         # данные

print("Данные экспортированы в students_export.csv")

conn.close()