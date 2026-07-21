import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator


BASE_PATH=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_PATH,'Test6.ui')

from_class=uic.loadUiType(UI_PATH)[0]

class WindowClass(QMainWindow,from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Test 6')
    
        for year in range(2000,2025+1):
            self.cbYear.addItem(str(year))
        
        for month in range(1,12+1):
            self.cbMonth.addItem(str(month))
        
        for day in range(1,31+1):
            self.cbDay.addItem(str(day))

        self.cbYear.setCurrentText(str(2000))
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.cbYear.currentIndexChanged.connect(self.printBirthDate)
        self.cbMonth.currentIndexChanged.connect(self.printBirthDate)
        self.cbDay.currentIndexChanged.connect(self.printBirthDate)

        self.calendarWidget.clicked.connect(self.selectDate)
    
    def selectDate(self):
        date=self.calendarWidget.selectedDate()

        year=date.toString('yyyy')
        month=date.toString('M')
        day=date.toString('d')
        print(year)
        self.cbYear.setCurrentText(year)
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)

        self.lineEdit.setText(year+'-'+month.zfill(2)+'-'+day.zfill(2))

    def printBirthDate(self):
        year=self.cbYear.currentText()
        month=self.cbMonth.currentText()
        day=self.cbDay.currentText()

        self.lineEdit.setText(year+'-'+month.zfill(2)+'-'+day.zfill(2))



if __name__ =="__main__":

    app=QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    sys.exit(app.exec())

    

