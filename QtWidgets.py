import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import *


class Example(QWidget):

    def __init__(self):
        super().__init__() #Функція super() повертає батьківський об'єкт Example з класом, і ми викликаємо його конструктор.
        self.resize(400, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('qt.png'))
        self.line = QLineEdit(self)
        self.line.move(10, 10)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())