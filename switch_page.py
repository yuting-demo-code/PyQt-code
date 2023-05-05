import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget

class Page1(QWidget):
    def __init__(self) -> None:
        super().__init__()
        verticalLayout_parent = QVBoxLayout(self)
        name = ["1", "2", "3"]
        self.pushButton = []
        for i in range(len(name)):
            pushButton = QPushButton(self)
            pushButton.setText(name[i])
            verticalLayout_parent.addWidget(pushButton)
            self.pushButton.append(pushButton)
            
        # self.return_btn = QPushButton("返回")
        # verticalLayout_parent.addWidget(self.return_btn)
            
class Page2(QWidget):
    def __init__(self) -> None:
        super().__init__()
        verticalLayout_parent = QVBoxLayout(self)
        name = ["4", "5", "6"]
        self.pushButton = []
        for i in range(len(name)):
            pushButton = QPushButton(self)
            pushButton.setText(name[i])
            verticalLayout_parent.addWidget(pushButton)
            self.pushButton.append(pushButton)
            
        self.return_btn = QPushButton("返回")
        verticalLayout_parent.addWidget(self.return_btn)
        
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # 創建堆疊小部件
        self.stacked_widget = QStackedWidget(self)

        # 創建兩個子小部件
        self.page1 = Page1()
        self.page2 = Page2()

        # 為按鈕添加事件處理器
        self.page1.pushButton[0].clicked.connect(self.switch_to_widget2)
        self.page2.return_btn.clicked.connect(self.switch_to_widget1)

        # 添加子小部件到堆疊小部件中
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # 在主窗口中添加堆疊小部件
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

    def switch_to_widget1(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(self.page1))

    def switch_to_widget2(self):
        self.stacked_widget.setCurrentIndex(self.stacked_widget.indexOf(self.page2))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())