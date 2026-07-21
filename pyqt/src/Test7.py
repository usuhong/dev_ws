import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator


BASE_PATH=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_PATH,'Test7.ui')

from_class=uic.loadUiType(UI_PATH)[0]

class windowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Test 7')

        self.editName.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.editGender.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name','Gender','BirthDate'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  #resize column

        self.btnAdd.clicked.connect(self.Add)

        regx=QRegularExpression("(F|M)")                #F나M을 찾는 정규표현식
        gender_validator=QRegularExpressionValidator(regx,self.editGender)  #해당 정규표현식을 가진 validator 생성
        self.editGender.setValidator(gender_validator)  #editGender에 적용
    
    def Add(self):
        if self.editName.text()=='' or self.editGender.text()=='':
            QMessageBox.warning(self,'warning','값이 입력되지 않았습니다')
        else:      
            row_index=self.table.rowCount()
            self.table.insertRow(row_index)
            texts=[self.editName.text(),self.editGender.text(),self.editBirthDate.text()]
            for idx, text in enumerate(texts):
                item=QTableWidgetItem(text)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(row_index,idx,item)

            self.editName.clear()
            self.editGender.clear()

if __name__=='__main__':

    app=QApplication(sys.argv)
    myWindows=windowClass()
    myWindows.show()
    sys.exit(app.exec())
