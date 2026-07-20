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

        self.hasDot=False

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
        self.Button_dot.clicked.connect(lambda: self.func('.'))
        

        self.Button0.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button7.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button8.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button9.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_equl.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_plus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_minus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_div.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_backs.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_clear.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Button_dot.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    # 키 입력 처리    
    def keyPressEvent(self, event):
        text=event.text()
        if text.isdigit():
            self.appendDigit(text)
        elif text in "+-*/":
            self.appendOperator(text)
        elif event.key()==Qt.Key.Key_Enter or Qt.Key.Key_Return:
            print("enter")
            self.calculate()
        elif event.key()==Qt.Key.Key_Backspace:
            print("backspace")
            self.back()
        elif event.key()==Qt.Key.Key_Escape:
            print("Escape")
            self.clear()

    def func(self,key):
        if key.isdigit():
            self.appendDigit(key)
        elif key in ('+', '-', '*', '/'):
            self.appendOperator(key)
        elif key=='=':
            self.calculate()
        elif key=="<":
            self.back()
        elif key=="C":
            self.clear()
        elif key=='.':
            self.appendDot()

    def appendDigit(self, key):
        self.expression+=key
        self.lineEdit_1.setText(self.expression)

    def appendOperator(self,key):
        self.hasDot=False
        if self.expression=='' and self.lastResult=='0':
            self.expression='0'
        
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
        except Exception:
            self.lineEdit_1.setText('잘못된 수식입니다!')
            return
        self.lineEdit_2.setText(self.value)
        self.lastResult=self.value
        self.expression=''
        self.lineEdit_1.clear()

    def back(self):
        if self.expression[-1]=='.':    #소수점을 지울 때 hasDot 변수 동기화
            self.hasDot=False
        self.expression=self.expression[:-1]
        self.lineEdit_1.setText(self.expression)
    
    def clear(self):
        self.expression=''
        self.value='0'
        self.lastResult='0'
        self.hasDot=False
        self.lineEdit_2.setText(self.value)
        self.lineEdit_1.setText(self.expression)
    
    def appendDot(self):
        print(self.hasDot)
        if self.hasDot==True:
            self.lineEdit_1.setText("이미 소수점이 있습니다")
            return
        if self.expression == '' or self.expression[-1] in '+-*/':
            self.expression += '0.'
        else:
            self.expression += '.'
        self.hasDot=True
        self.lineEdit_1.setText(self.expression)



if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())