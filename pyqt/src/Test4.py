import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_PATH,"Test4.ui")

from_class=uic.loadUiType(UI_PATH)[0]


class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test 4")
        

        self.outputText.setReadOnly(True)
        self.addButton.clicked.connect(self.addText)
        self.clearButton.clicked.connect(self.clearText)
        self.ubuntuButton.clicked.connect(lambda : self.setFont("Ubuntu"))
        self.nanumButton.clicked.connect(lambda : self.setFont("NanumGothic"))
        self.redButton.clicked.connect(lambda : self.setTextColor(255,0,0))
        self.blueButton.clicked.connect(lambda : self.setTextColor(0,0,255))
        self.greenButton.clicked.connect(lambda : self.setTextColor(0,255,0))
        self.fontSizeButton.clicked.connect(self.setTextSize)

        self.fontSizeLine.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.fontSizeLine.returnPressed.connect(self.setTextSize)
        self.fontSizeLine.setValidator(QIntValidator())
        
    def addText(self):
        input=self.inputText.toPlainText()
        self.outputText.append(input)
        self.inputText.clear()
    
    def clearText(self):
        self.outputText.clear()
    
    def setFont(self, fontName):
        font=QFont(fontName,11)
        self.outputText.setFont(font)
    
    def setTextColor(self,r,g,b):
        color=QColor(r,g,b)
        self.outputText.selectAll()
        self.outputText.setTextColor(color)
        self.outputText.moveCursor(QTextCursor.MoveOperation.End)
    
    def setTextSize(self):
        size=int(self.fontSizeLine.text())
        self.outputText.selectAll()
        self.outputText.setFontPointSize(size)
        self.outputText.moveCursor(QTextCursor.MoveOperation.End)


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())