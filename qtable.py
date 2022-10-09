# https://zhuanlan.zhihu.com/p/34532247
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QColor
# from faker import Factory
import random
import sys
class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.id = 1
        self.lines = []
        self.editable = True
        self.des_sort = True
        # self.faker = Factory.create()
        self.btn_add.clicked.connect(self.add_line)
        self.btn_del.clicked.connect(self.del_line)
        self.btn_modify.clicked.connect(self.modify_line)
        self.btn_set_header.clicked.connect(self.setheader)
        self.table.cellChanged.connect(self.cellchange)
#     # Sess = sessionmaker(bind = engine)
    def setupUI(self):
        self.setWindowTitle('QTableWidget')
        self.resize(640,480)
        self.table = QTableWidget(self)
        self.btn_add = QPushButton('add')
        self.btn_del = QPushButton('remove')
        self.btn_modify = QPushButton('可以編輯')
        self.btn_set_header = QPushButton('標頭設置')
  
        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn_add)
        self.vbox.addWidget(self.btn_del)
        self.vbox.addWidget(self.btn_modify)
        self.vbox.addWidget(self.btn_set_header)
        self.vbox.addSpacerItem(self.spacerItem)  #可以用addItem也可以用addSpacerItem方法添加，沒看出哪裡不一樣
        self.txt = QLabel()
        self.txt.setMinimumHeight(50)
        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.table)
        self.vbox2.addWidget(self.txt)
        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox2)
        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)
        self.table.setColumnCount(4)   ##设置列数
        self.headers = ['id','選擇','姓名','成績','住址']
        self.table.setHorizontalHeaderLabels(self.headers)
        self.show()
    def add_line(self):
        self.table.cellChanged.disconnect()
        row = self.table.rowCount()
        self.table.setRowCount(row + 1)
        id = str(self.id)
        ck = QCheckBox()
        h = QHBoxLayout()
        h.setAlignment(Qt.AlignCenter)
        h.addWidget(ck)
        w = QWidget()
        w.setLayout(h)
        name = str(random.randint(50,99))
        score = str(random.randint(50,99))
        add = str(random.randint(50,99))
        self.table.setItem(row,0,QTableWidgetItem(id))
        self.table.setCellWidget(row,1,w)
        self.table.setItem(row,2,QTableWidgetItem(name))
        self.table.setItem(row,3,QTableWidgetItem(score))
        self.table.setItem(row,4,QTableWidgetItem(add))
        self.id += 1
        self.lines.append([id,ck,name,score,add])
        self.settext('自動生成隨機一行數據！ ,checkbox設置為居中顯示')
        self.table.cellChanged.connect(self.cellchange)
    def del_line(self):
        removeline = []
        for line in self.lines:
            if line[1].isChecked():
                row = self.table.rowCount()
                for x in range(row,0,-1):
                    if line[0] == self.table.item(x - 1,0).text():
                        self.table.removeRow(x - 1)
                        removeline.append(line)
        for line in removeline:
            self.lines.remove(line)
        self.settext('刪除在左邊checkbox中選中的行，使用了一個笨辦法取得行號\n，不知道有沒有其他可以直接取得行號的方法！')
    def modify_line(self):
        if self.editable == True:
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.btn_modify.setText('禁止編輯')
            self.editable = False
        else:
            self.table.setEditTriggers(QAbstractItemView.AllEditTriggers)
            self.btn_modify.setText('可以編輯')
            self.editable = True
        self.settext('設置，是否可以編輯整個表格')
    def select_line(self):
        if self.table.selectionBehavior() == 0:
            self.table.setSelectionBehavior(1)
            self.btn_select_line.setStyleSheet('background-color:lightblue')
        else:
            self.table.setSelectionBehavior(0)
            self.btn_select_line.setStyleSheet('')
        self.settext('默認時，點擊單元格，只可選擇一個格，此處設置為可選擇整行')

    def deny_muti_line(self):
        if self.table.selectionMode() in [2,3]:
            self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            self.btn_select_single.setStyleSheet('background-color:lightblue')
        else:
            self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.btn_select_single.setStyleSheet('')
        self.settext('點擊時會輪換以多行或單行選擇，默認是可以同時選擇多行')
    def sortItem(self):
        if self.des_sort == True:
            self.table.sortItems(3,Qt.DescendingOrder)
            self.des_sort = False
            self.btn_sort.setStyleSheet('background-color:lightblue')
            self.table.setSortingEnabled(True)  # 设置表头可以自动排序
        else:
            self.table.sortItems(3,Qt.AscendingOrder)
            self.des_sort = True
            self.btn_sort.setStyleSheet('background-color:lightblue')
            self.table.setSortingEnabled(False)
        self.settext('點擊時會輪換以升序降序排列，但排序時，會使自動列寬失效！')
    def setheader(self):
        font = QFont('微軟正黑體', 12)
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)  # 设置表头字体
        self.table.setColumnWidth(0,50)
        self.table.setColumnWidth(1,50)
        self.table.setColumnWidth(3,100)
        self.table.horizontalHeader().setSectionResizeMode(2,QHeaderView.Stretch)
        self.table.horizontalHeader().setStyleSheet('QHeaderView::section{background:gray}')
        self.table.horizontalHeader().setFixedHeight(50)
        self.table.setColumnHidden(0,True)
        self.btn_set_header.setStyleSheet('background-color:lightblue')
        self.settext('設置標頭字體及字號，隱藏ID列，設置標頭除姓名外全部為固定寬度\n，設置姓名列自動擴展寬度，設置標頭行高，設置標頭背景色')
    def middle(self):
        self.btn_set_middle.setStyleSheet('background-color:lightblue')
        self.table.setStyleSheet('color:green;')
        row = self.table.rowCount()
        for x in range(row):
            for y in range(4):
                if y != 1:
                    item = self.table.item(x,y)
                    item.setTextAlignment(Qt.AlignCenter)
                else:
                    pass
        self.btn_set_middle.setStyleSheet('background-color:lightblue')
        self.settext('將文字居中顯示,設置文字顏色')
    def cellchange(self,row,col):
        item = self.table.item(row,col)
        txt = item.text()
        self.settext('第%s行，第%s列 , 數據改變為:%s'%(row,col,txt))
    def noframe(self):
        self.table.setAlternatingRowColors(True)
        self.table.setFrameStyle(QFrame.NoFrame)
        self.table.setStyleSheet('color:green;'
                                 'gridline-color:white;'
                                 'border:0px solid gray')
        self.settext('取消表的框線,\n 取消表格內框')

    def settext(self,txt):
        font = QFont('微軟正黑體',10)
        self.txt.setFont(font)
        self.txt.setText(txt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ui()
    sys.exit(app.exec_())