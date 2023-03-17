import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

class MyCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Starry Night')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        
        # background
        painter.fillRect(0, 0, 800, 600, QColor(17, 30, 108))
        
        # moon
        painter.setBrush(QBrush(QColor(255, 242, 0), Qt.SolidPattern))
        painter.drawEllipse(200, 100, 120, 120)
        
        # stars
        painter.setBrush(QBrush(QColor(255, 255, 255), Qt.SolidPattern))
        painter.drawEllipse(500, 200, 10, 10)
        painter.drawEllipse(600, 150, 10, 10)
        painter.drawEllipse(350, 50, 10, 10)
        painter.drawEllipse(400, 200, 10, 10)
        painter.drawEllipse(250, 250, 10, 10)
        painter.drawEllipse(450, 300, 10, 10)
        painter.drawEllipse(100, 400, 10, 10)
        painter.drawEllipse(300, 450, 10, 10)
        painter.drawEllipse(550, 400, 10, 10)
        painter.drawEllipse(700, 450, 10, 10)
        painter.drawEllipse(750, 250, 10, 10)
        painter.drawEllipse(50, 200, 10, 10)
        
        # buildings
        painter.setBrush(QBrush(QColor(0, 0, 0), Qt.SolidPattern))
        painter.drawRect(50, 300, 100, 150)
        painter.drawRect(200, 250, 100, 200)
        painter.drawRect(350, 350, 150, 100)
        painter.drawRect(550, 250, 100, 200)
        painter.drawRect(700, 300, 100, 150)
       
        # windows
        painter.setBrush(QBrush(QColor(255, 255, 255), Qt.SolidPattern))
        painter.drawEllipse(70, 320, 30, 30)
        painter.drawEllipse(110, 320, 30, 30)
        painter.drawEllipse(70, 360, 30, 30)
        painter.drawEllipse(110, 360, 30, 30)
        painter.drawEllipse(220, 270, 30, 30)
        painter.drawEllipse(260, 270, 30, 30)
        painter.drawEllipse(370, 370, 30, 30)
        pen = QPen(QColor(69, 69, 69), 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor(191, 255, 255), Qt.SolidPattern))
        painter.drawRect(200, 200, 200, 200)

        # window panels
        pen = QPen(QColor(69, 69, 69), 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor(255, 255, 191), Qt.SolidPattern))
        painter.drawRect(220, 220, 80, 80)
        painter.drawRect(300, 220, 80, 80)
        painter.drawRect(220, 300, 80, 80)
        painter.drawRect(300, 300, 80, 80)

        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyCanvas()
    sys.exit(app.exec_())