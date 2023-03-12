import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt

class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400) # 위치와 크기 설정/ 파리미터 변경
        self.setWindowTitle('My_Canvas') #  gui이름 정하기
        self.show() # 출력

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(QColor(150, 150, 150), 10, Qt.SolidLine) # HSV Color Format ( 0~255 ) , size(10)
        painter.setPen(pen) # 색 지점 출력
        painter.drawPoint(100, 100) , painter.drawPoint(500, 300) , painter.drawPoint(500, 300) # 점 그리기
        painter.drawPoint(200, 100) , painter.drawPoint(300, 200) , painter.drawPoint(500, 300)
        painter.drawPoint(400, 500) , painter.drawPoint(500, 200) , painter.drawPoint(500, 300)
        painter.drawPoint(500, 300) , painter.drawPoint(500, 300) , painter.drawPoint(500, 300)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyCanvas()
    sys.exit(app.exec_())
