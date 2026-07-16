import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_DIR,"Test2.ui")

from_class=uic.loadUiType(UI_PATH)[0]

class WindowClass(QMainWindow,from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test2")
        self.countButton.clicked.connect(self.increment)
        self.resetButton.clicked.connect(self.countReset)
        self.submitButton.clicked.connect(self.submit)
        self.inputLine.returnPressed.connect(self.changeOutput)

        self.cnt=0
        self.label.setText(str(self.cnt))
        self.outputLine.setReadOnly(True)
    
    def increment(self):
        self.cnt+=1
        self.label.setText(str(self.cnt))
    
    def countReset(self):
        self.cnt=0
        self.label.setText(str(self.cnt))
    
    def submit(self):
        self.label.setText(self.lineEdit.text())
        self.lineEdit.clear()

    def changeOutput(self):
        self.outputLine.setText(self.inputLine.text())
    
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())