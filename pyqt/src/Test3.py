import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_DIR,"Test3.ui")

from_class=uic.loadUiType(UI_PATH)[0]

class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test 3")
        self.addButton.clicked.connect(self.addText)
        self.inputLine.returnPressed.connect(self.addText)
        self.clearButton.clicked.connect(self.clearText)

    def addText(self):
        self.outputText.append(self.inputLine.text())
        self.inputLine.clear()
    
    def clearText(self):
        self.outputText.clear()


if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())
