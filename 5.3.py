import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QProgressBar,
                             QPushButton, QVBoxLayout)
from PyQt5.QtCore import QTimer


class ProgressBarWindow(QWidget):
    """Окно с прогрессбаром и кнопкой для его заполнения."""
    def __init__(self):
        super().__init__()
        self.initUI()
        self.progress = 0

    def initUI(self):
        self.setWindowTitle('Задание 6: Прогрессбар')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.progressBar = QProgressBar(self)
        self.progressBar.setValue(0)
        layout.addWidget(self.progressBar)

        self.button = QPushButton('Старт', self)
        self.button.clicked.connect(self.start_progress)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def start_progress(self):
        self.progress = 0
        self.progressBar.setValue(0)
        self.button.setEnabled(False)
        self.timer.start(100)  # обновление каждые 100 мс

    def update_progress(self):
        self.progress += 1
        self.progressBar.setValue(self.progress)
        if self.progress >= 100:
            self.timer.stop()
            self.button.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBarWindow()
    window.show()
    sys.exit(app.exec_())