import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Sample(QWidget):

    def __init__(self):
        super().__init__() #Функція super() повертає батьківський об'єкт Example з класом, і ми викликаємо його конструктор.
        self.resize(400, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('qt.png'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Sample()
    sys.exit(app.exec_())