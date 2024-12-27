import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Github Drawing")
        self.setGeometry(100, 100, 400, 400)  

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        p.setPen(QColor(0, 0, 0))  
        p.setBrush(QColor(0, 127, 0))  

        triangle_points = [
            QPoint(200, 50),  
            QPoint(100, 250), 
            QPoint(300, 250), 
        ]
        
        p.drawPolygon(QPolygon(triangle_points))
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window3()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
