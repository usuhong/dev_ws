import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_PATH,"Test5.ui")

from_class=uic.loadUiType(UI_PATH)[0]


class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("TEstE 5")


        self.textEdit.setReadOnly(True)
        self.btnName.clicked.connect(self.inputName)
        self.btnSeason.clicked.connect(self.inputSeason)
        self.btnColor.clicked.connect(self.inputColor)
        self.btnFont.clicked.connect(self.inputFont)
        self.btnFile.clicked.connect(self.openFile)
        self.lineEdit.returnPressed.connect(self.inputNumber)
    
    def inputName(self):
        text,ok=QInputDialog.getText(self,'qDialoog-Name','User Name')

        if ok and text:
            self.textEdit.append(text)
            print(ok,text)
    
    def inputSeason(self):

        items=['Spring','Summer','Fall','Winter']

        item,ok=QInputDialog.getItem(self,'Title','Seasons',items,0,False)

        if item and ok:
            self.textEdit.append(item)
    
    def inputColor(self):

        color=QColorDialog().getColor()

        if color.isValid():
            self.textEdit.append('Color')
            self.textEdit.selectAll()
            self.textEdit.setTextColor(color)
            self.textEdit.moveCursor(QTextCursor.MoveOperation.End)

    
    def inputFont(self):
        
        font,ok=QFontDialog().getFont()

        if ok and font:
            info=QFontInfo(font)
            self.textEdit.append(info.family() + info.styleName())
            self.textEdit.selectAll()
            self.textEdit.setFont(font)
            self.textEdit.moveCursor(QTextCursor.MoveOperation.End)

    def openFile(self):

        name=QFileDialog.getOpenFileName(self,'Open File','./')
        print(name)
        if name[0]:                         #파일을 선택했으면
            with open(name[0],'r') as file: #선택한 파일을 읽기모드로 열고
                data=file.read()            #파일의 내용을 읽어서 dataㅇ에 저장
                self.textEdit.append(data)  #출력


    def inputNumber(self):
        
        mes=self.lineEdit.text()
        if mes.isdigit():
            self.textEdit.append(mes)
        else:
            retval= QMessageBox.question(self,'QMessageBox- question','Are you sure to print?',
                                 QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes,
                                QMessageBox.StandardButton.Yes)
            if retval==QMessageBox.StandardButton.Yes:
                self.textEdit.append(mes)

        self.lineEdit.clear()

        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())