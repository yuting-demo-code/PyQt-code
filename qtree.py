import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt
class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(TreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')
        self.tree=QTreeWidget()
        #设置列数
        self.tree.setHeaderHidden( True )
        #设置根节点
        root1=QTreeWidgetItem(self.tree)
        root1.setText(0,'Root')
        root2=QTreeWidgetItem(self.tree)
        root2.setText(0,'Root2')
        #设置树形控件的列的宽度
        self.tree.setColumnWidth(0,150)
        #设置子节点1
        child1=QTreeWidgetItem()
        child1.setText(0,'child1')
        root1.addChild(child1)
        #设置子节点2
        child2=QTreeWidgetItem(root2)
        child2.setText(0,'child2')
        #设置子节点3
        child3=QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        #加载根节点的所有属性与子控件
        self.tree.addTopLevelItem(root1)
        self.tree.addTopLevelItem(root2)
        #TODO 优化3 给节点添加响应事件
        self.tree.clicked.connect(self.onClicked)
        #节点全部展开
        self.setCentralWidget(self.tree)

    def onClicked(self,qmodeLindex):
        item=self.tree.currentItem()
        print('Key=%s,value=%s'%(item.text(0),item.text(1)))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())