import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import Qt

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_DIR,"calculator.ui")

from_class=uic.loadUiType(UI_PATH)[0]

class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")
        
        self.value='0'
        self.expression=''

        self.key='0'
        self.lastResult='0'

        self.lineEdit_1.setReadOnly(True)
        self.lineEdit_1.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.lineEdit_1.setText(self.expression)
        self.lineEdit_2.setText(self.value)
        self.Button0.clicked.connect(lambda: self.func('0'))
        self.Button1.clicked.connect(lambda: self.func('1'))
        self.Button2.clicked.connect(lambda: self.func('2'))
        self.Button3.clicked.connect(lambda: self.func('3'))
        self.Button4.clicked.connect(lambda: self.func('4'))
        self.Button5.clicked.connect(lambda: self.func('5'))
        self.Button6.clicked.connect(lambda: self.func('6'))
        self.Button7.clicked.connect(lambda: self.func('7'))
        self.Button8.clicked.connect(lambda: self.func('8'))
        self.Button9.clicked.connect(lambda: self.func('9'))
        self.Button_equl.clicked.connect(lambda: self.func('='))
        self.Button_plus.clicked.connect(lambda: self.func('+'))
        self.Button_minus.clicked.connect(lambda: self.func('-'))
        self.Button_mul.clicked.connect(lambda: self.func('*'))
        self.Button_div.clicked.connect(lambda: self.func('/'))
        self.Button_backs.clicked.connect(lambda: self.func('<'))
        self.Button_clear.clicked.connect(lambda: self.func('C'))
    
    def func(self,key):
        if key.isdigit():
            self.appendDigit(key)
        elif key in ('+', '-', '*', '/'):
            self.appendOperator(key)
        elif key=='=':
            self.calculate()
        else:
            self.modify(key)

    def appendDigit(self, key):
        self.expression+=key
        self.lineEdit_1.setText(self.expression)

    def appendOperator(self,key):
        if self.expression=='' and self.lastResult=='0':
            self.lineEdit_1.setText("잘못된 수식입니다!")
            return
        elif self.expression=='' and self.lastResult!='0':
            self.expression=self.lastResult
        lastInput=self.expression[-1]        #마지막 입력을 불러옴

        if lastInput.isdigit():
            self.expression+=key
        else:
            self.expression=self.expression[:-1]+key
        self.lineEdit_1.setText(self.expression)
    
    def calculate(self):
        if self.expression=='':
            self.lineEdit_1.setText("잘못된 수식입니다!")
            return
        try:
            result=eval(self.expression)
            self.value=str(result)
        except ZeroDivisionError:
            self.lineEdit_1.setText("0으로 나눌 수 없습니다!")
            self.expression = ''
            return
        self.lineEdit_2.setText(self.value)
        self.lastResult=self.value
        self.expression=''
        self.lineEdit_1.clear()

    def modify(self,key):
        if key=='C':
            self.expression=''
            self.value='0'
            self.lastResult='0'
            self.lineEdit_2.setText(self.value)
        elif key=='<':
            self.expression=self.expression[:-1]
        

        self.lineEdit_1.setText(self.expression)




if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())