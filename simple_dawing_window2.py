import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class SimpleDrawingWindow2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple GitHub Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 127, 0))
        p.setBrush(QColor(255, 127, 0))

        p.drawEllipse(QPoint(100, 100), 50, 50)  

        p.end()

def main():
    app = QApplication(sys.argv)

    w = SimpleDrawingWindow2()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
