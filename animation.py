import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
 
 
class AnimWindow(QWidget):
    def __init__(self, parent=None):
        super(AnimWindow, self).__init__(parent)
        self.btn = QPushButton('Exit', self)
        self.animation = None
        self.animation2 = None
        self.draw_ui()
 
    def draw_ui(self):
        self.setGeometry(0, 0, 1024, 600)
        self.btn.setGeometry(50, 50, 100, 50)
        self.btn.clicked.connect(self.close)
 
    def closeEvent(self, event):
        if self.animation is None and self.animation2 is None:
            self.animation = QPropertyAnimation(self, b'geometry')
            self.animation2 = QPropertyAnimation(self, b'windowOpacity')
            self.animation.setStartValue(QRect(0, 0, self.width(), self.height()))
            self.animation.setEndValue(QRect(1024, 600, 0, 0))
            self.animation2.setStartValue(1)
            self.animation2.setEndValue(0)
            self.animation.finished.connect(self.close)
            self.animation2.finished.connect(self.close)
            self.animation.setDuration(1500)
            self.animation.start()
            self.animation2.setDuration(1500)
            self.animation2.start()
            event.ignore()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimWindow()
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.show()
    sys.exit(app.exec_())