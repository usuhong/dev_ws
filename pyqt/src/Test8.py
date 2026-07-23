import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import Qt

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_PATH,'Test8.ui')

from_class=uic.loadUiType(UI_PATH)[0]

class windowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Test8')

        #오른쪽 정렬
        self.editMin.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.editMax.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.editStep.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.spinBoxValue.setAlignment(Qt.AlignmentFlag.AlignRight)

        #숫자형만 입력
        self.editMin.setValidator(QIntValidator())
        self.editMax.setValidator(QIntValidator())
        self.editStep.setValidator(QIntValidator())

        
        min=self.spinBox.minimum()
        max=self.spinBox.maximum()
        step=self.spinBox.singleStep()

        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))

        self.slider.setRange(int(min),int(max))
        self.slider.setSingleStep(int(step))

        self.btnApply.clicked.connect(self.Apply)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        self.slider.valueChanged.connect(self.changeSlide)


    def Apply(self):
        min=self.editMin.text()
        max=self.editMax.text()
        step=self.editStep.text()

        self.spinBox.setRange(int(min),int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min),int(max))
        self.slider.setSingleStep(int(step))

    def changeSpinBox(self):
        value=self.spinBox.value()
        self.spinBoxValue.setText(str(value))
        self.slider.setValue(value)
    
    def changeSlide(self):
        value=self.slider.value()
        self.sliderValue.setText(str(value))
        self.spinBox.setValue(value)
if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindows=windowClass()
    myWindows.show()
    sys.exit(app.exec())
