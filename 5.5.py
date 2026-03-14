import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime


class TimerApp(QWidget):
    """Секундомер с возможностью запуска, паузы и сброса."""
    def __init__(self):
        super().__init__()
        self.initUI()
        self.time = QTime(0, 0, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.running = False

    def initUI(self):
        self.setWindowTitle('Задание 5: Таймер/Секундомер')
        self.setGeometry(100, 100, 300, 150)

        main_layout = QVBoxLayout()

        self.label = QLabel('00:00:00', self)
        self.label.setStyleSheet('font-size: 30pt; font-family: monospace;')
        main_layout.addWidget(self.label)

        btn_layout = QHBoxLayout()

        self.start_btn = QPushButton('Старт')
        self.start_btn.clicked.connect(self.start)
        btn_layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton('Стоп')
        self.stop_btn.clicked.connect(self.stop)
        btn_layout.addWidget(self.stop_btn)

        self.reset_btn = QPushButton('Сброс')
        self.reset_btn.clicked.connect(self.reset)
        btn_layout.addWidget(self.reset_btn)

        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

    def start(self):
        if not self.running:
            self.timer.start(1000)  # обновление каждую секунду
            self.running = True
            self.start_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)

    def stop(self):
        if self.running:
            self.timer.stop()
            self.running = False
            self.start_btn.setEnabled(True)
            self.stop_btn.setEnabled(False)

    def reset(self):
        self.timer.stop()
        self.running = False
        self.time = QTime(0, 0, 0)
        self.label.setText(self.time.toString('hh:mm:ss'))
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)

    def update_time(self):
        self.time = self.time.addSecs(1)
        self.label.setText(self.time.toString('hh:mm:ss'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimerApp()
    window.show()
    sys.exit(app.exec_())