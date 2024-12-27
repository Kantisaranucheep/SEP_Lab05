import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from triangle import Simple_drawing_window3
from circle import SimpleDrawingWindow2
from square import Simple_drawing_window1

class DrawingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Drawing Program")
        self.setGeometry(100, 100, 400, 400)

        self.triangle = Simple_drawing_window3()
        self.circle = SimpleDrawingWindow2()
        self.square = Simple_drawing_window1()

        layout = QVBoxLayout()
        layout.addWidget(self.triangle)
        layout.addWidget(self.circle)
        layout.addWidget(self.square)

        self.setLayout(layout)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.end()

def main():
    app = QApplication(sys.argv)
    window = DrawingWindow()
    window.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
