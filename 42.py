import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
 

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('42.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.graphicsView.clear)
        
    def run(self):
        #try:
            self.graphicsView.plot([eval(self.lineEdit.text()) for x in eval(f'range({self.lineEdit_2.text()})')])
        #except:
            #print('error', self.lineEdit.text(), self.lineEdit_2.text())

 

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
