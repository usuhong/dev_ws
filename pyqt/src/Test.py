import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import *

#실행 위치와 상관없이 동작하도록 현재 Python 파일의 위치(__file__)를 기준으로 .ui 파일 경로만듬
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
UI_PATH=os.path.join(BASE_DIR,"Test.ui")

from_class=uic.loadUiType(UI_PATH)[0]
temp=uic.loadUiType(UI_PATH)[1]
print(from_class)
print(temp)
class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test PyQt");
        self.textEdit.setText("This is text editor.")

        self.button1.clicked.connect(self.clickButton1)
        self.button2.clicked.connect(self.clickButton2)
        self.button3.clicked.connect(self.clickButton3)

        self.radioButton1.clicked.connect(self.clickRadio)
        self.radioButton2.clicked.connect(self.clickRadio)
        self.radioButton3.clicked.connect(self.clickRadio)

        self.checkBox1.clicked.connect(self.toggleCheckBox1)
        self.checkBox2.clicked.connect(self.toggleCheckBox2)
        self.checkBox3.clicked.connect(self.toggleCheckBox3)

        self.checkBox4.setEnabled(False)
        self.checkBox5.setEnabled(False)
        self.checkBox6.setEnabled(False)
        

    def clickButton1(self):
        self.textEdit.setText("Button 1")
        self.radioButton1.setChecked(True)
    def clickButton2(self):
        self.textEdit.setText("Button 2")
        self.radioButton2.setChecked(True)
    def clickButton3(self):
        self.textEdit.setText("Button 3")
        self.radioButton3.setChecked(True)
    
    def clickRadio(self):
        if self.radioButton1.isChecked():     self.textEdit.setText("Radio 1")
        elif self.radioButton2.isChecked():     self.textEdit.setText("Radio 2")
        elif self.radioButton3.isChecked():     self.textEdit.setText("Radio 3")
        else:   self.textEdit.setText("Unknown")

    def toggleCheckBox1(self):
        self.textEdit.setText("CheckBox 1")
        self.checkBox4.setChecked(self.checkBox1.isChecked())
    def toggleCheckBox2(self):
        self.textEdit.setText("CheckBox 2")
        self.checkBox5.setChecked(self.checkBox2.isChecked())
    def toggleCheckBox3(self):
        self.textEdit.setText("CheckBox 3")
        self.checkBox6.setChecked(self.checkBox3.isChecked())
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())

