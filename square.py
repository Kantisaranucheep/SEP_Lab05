import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")

    def paintEvent(self, e):
        p = QPainter(self)
        p.begin(self)

        # Drawing a Square
        p.setPen(QColor(0, 0, 255)) 
        p.setBrush(QColor(0, 0, 255, 50)) 
        p.drawRect(200, 100, 50, 50)

        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window1()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
