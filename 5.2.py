import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit,
                             QPushButton, QVBoxLayout, QMessageBox)


class TextFieldWindow(QWidget):
    """Окно с полем ввода и кнопкой, показывающей введённый текст."""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Задание 2: Поле ввода')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText('Введите текст...')
        layout.addWidget(self.edit)

        self.button = QPushButton('Показать текст', self)
        self.button.clicked.connect(self.show_text)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_text(self):
        text = self.edit.text()
        if text:
            QMessageBox.information(self, 'Введённый текст', text)
        else:
            QMessageBox.warning(self, 'Предупреждение', 'Поле пустое!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextFieldWindow()
    window.show()
    sys.exit(app.exec_())