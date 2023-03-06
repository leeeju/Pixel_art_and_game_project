import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QColorDialog
from PyQt5.QtGui import QPainter, QPen, QColor, QImage
from PyQt5.QtCore import Qt


class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Paint App')
        self.image = None
        self.color = QColor(0, 0, 0)
        self.pen_size = 5

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw_point(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.draw_point(event)

    def draw_point(self, event):
        if self.image is None:
            self.image = QImage(self.width(), self.height(), QImage.Format_RGB32)
            self.image.fill(Qt.white)
        painter = QPainter(self.image)
        painter.setPen(QPen(self.color, self.pen_size, Qt.SolidLine))
        painter.drawPoint(event.pos())
        self.update()

    def paintEvent(self, event):
        if self.image is not None:
            painter = QPainter(self)
            painter.drawImage(self.rect(), self.image, self.image.rect())

    def set_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

    def set_pen_size(self, size):
        self.pen_size = size


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.paint_widget = PaintWidget()
        self.setCentralWidget(self.paint_widget)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Paint App')
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()
        self.show()

    def create_menu(self):
        menu = self.menuBar().addMenu('File')
        menu.addAction('Exit', self.close)
        options_menu = self.menuBar().addMenu('Options')
        color_action = options_menu.addAction('Color')
        color_action.triggered.connect(self.paint_widget.set_color)
        pen_size_menu = options_menu.addMenu('Pen Size')
        for size in [1, 3, 5, 7, 9]:
            pen_size_action = pen_size_menu.addAction(str(size))
            pen_size_action.triggered.connect(lambda _, s=size: self.paint_widget.set_pen_size(s))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

