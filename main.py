import random
import sys

from PyQt5 import QtWidgets, uic

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPolygon, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

import Ui


class Main(QMainWindow, Ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('Ui.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_click)

    def button_click(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(random.choice(['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                                           'Blue', 'Magenta', 'Purple', 'Brown', 'Black'])))
        o = random.randint(1, 500)
        qp.drawEllipse(
            500 - o // 2, 500 - o // 2, o, o
        )
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
