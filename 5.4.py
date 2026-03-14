import sys
import json
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QListWidget, QTextEdit, QPushButton, QInputDialog,
                             QMessageBox, QFileDialog)


class NotesApp(QWidget):
    """Приложение для заметок с сохранением в JSON-файл."""
    def __init__(self):
        super().__init__()
        self.notes = {}
        self.current_note = None
        self.filename = 'notes.json'
        self.initUI()
        self.load_notes()

    def initUI(self):
        self.setWindowTitle('Задание 1: Заметки')
        self.setGeometry(100, 100, 600, 400)

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self.listWidget = QListWidget()
        self.listWidget.itemClicked.connect(self.on_note_selected)
        left_layout.addWidget(self.listWidget)

        btn_add = QPushButton('Добавить')
        btn_add.clicked.connect(self.add_note)
        left_layout.addWidget(btn_add)

        btn_delete = QPushButton('Удалить')
        btn_delete.clicked.connect(self.delete_note)
        left_layout.addWidget(btn_delete)

        main_layout.addLayout(left_layout, 1)

        right_layout = QVBoxLayout()
        self.textEdit = QTextEdit()
        right_layout.addWidget(self.textEdit)

        btn_save = QPushButton('Сохранить')
        btn_save.clicked.connect(self.save_current_note)
        right_layout.addWidget(btn_save)

        main_layout.addLayout(right_layout, 2)

        self.setLayout(main_layout)

    def load_notes(self):
        """Загрузка заметок из файла."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.notes = json.load(f)
                self.update_list()
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка', f'Не удалось загрузить заметки: {e}')
        else:
            self.notes = {}

    def save_notes(self):
        """Сохранение заметок в файл."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.notes, f, ensure_ascii=False, indent=2)
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Не удалось сохранить заметки: {e}')

    def update_list(self):
        """Обновление списка заметок."""
        self.listWidget.clear()
        self.listWidget.addItems(self.notes.keys())

    def add_note(self):
        """Добавление новой заметки."""
        title, ok = QInputDialog.getText(self, 'Новая заметка', 'Введите название:')
        if ok and title:
            if title in self.notes:
                QMessageBox.warning(self, 'Ошибка', 'Заметка с таким названием уже существует!')
            else:
                self.notes[title] = ''
                self.update_list()
                self.save_notes()

    def delete_note(self):
        """Удаление выбранной заметки."""
        current = self.listWidget.currentItem()
        if current:
            title = current.text()
            reply = QMessageBox.question(self, 'Подтверждение',
                                         f'Удалить заметку "{title}"?',
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                del self.notes[title]
                self.update_list()
                self.textEdit.clear()
                self.current_note = None
                self.save_notes()

    def on_note_selected(self, item):
        """При выборе заметки из списка загружаем её текст в редактор."""
        title = item.text()
        self.current_note = title
        self.textEdit.setText(self.notes.get(title, ''))

    def save_current_note(self):
        """Сохраняет текущий текст в выбранную заметку."""
        if self.current_note:
            self.notes[self.current_note] = self.textEdit.toPlainText()
            self.save_notes()
            QMessageBox.information(self, 'Сохранено', 'Заметка сохранена.')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Сначала выберите заметку.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotesApp()
    window.show()
    sys.exit(app.exec_())