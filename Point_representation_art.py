import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt

class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500) # 위치와 크기 설정
        self.setWindowTitle('My_Canvas')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(QColor(0, 0, 0), 5, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawPoint(100, 100) # 점 그리기
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyCanvas()
    sys.exit(app.exec_())
