import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class SimpleWindow(QWidget):
    """Простейшее окно с кнопкой и надписью."""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Задание 10: Простейший GUI')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Нажми кнопку', self)
        layout.addWidget(self.label)

        self.button = QPushButton('Привет', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_click(self):
        self.label.setText('Привет, PyQt5!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())