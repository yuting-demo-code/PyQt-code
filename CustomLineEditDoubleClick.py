from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
    def mouseDoubleClickEvent(self, event):
        super().mouseDoubleClickEvent(event)
        self.setReadOnly(False)  # Enable editing when double-clicked
        
    def mousePressEvent(self, event):
        self.setReadOnly(True)  # Set ReadOnly to True when clicked outside the line edit
        super().mousePressEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = QMainWindow()
    centralWidget = QWidget(mainWindow)
    layout = QHBoxLayout(centralWidget)

    lineEdit = CustomLineEdit(centralWidget)  # Use CustomLineEdit instead of QLineEdit

    layout.addWidget(lineEdit)
    mainWindow.setCentralWidget(centralWidget)
    mainWindow.show()

    sys.exit(app.exec_())
