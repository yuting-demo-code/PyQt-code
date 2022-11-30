import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SliderDemo(QWidget):
    def __init__(self,parent=None):
        super(SliderDemo, self).__init__(parent)
        #設置標題與初始大小
        self.setWindowTitle('QSlider例子')
        self.resize(300,100)

        #垂直佈局
        layout=QVBoxLayout()

        #創建標籤，居中
        self.l1=QLabel('Hello PyQt5')
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)
        #創建水平方向滑動條
        self.s1=QSlider(Qt.Horizontal)
        ##設置最小值
        self.s1.setMinimum(10)
        #設置最大值
        self.s1.setMaximum(50)
        #步長
        self.s1.setSingleStep(3)
        #設置當前值
        self.s1.setValue(20)
        #刻度位置，刻度下方
        self.s1.setTickPosition(QSlider.TicksBelow)
        #設置刻度間距
        self.s1.setTickInterval(5)
        layout.addWidget(self.s1)
        #設置連接信號槽函數
        self.s1.valueChanged.connect(self.valuechange)

        self.setLayout(layout)

    def valuechange(self):
        #輸出當前地刻度值，利用刻度值來調節字體大小
        print('current slider value=%s'%self.s1.value())
        size=self.s1.value()
        self.l1.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=SliderDemo()
    demo.show()
    sys.exit(app.exec_())