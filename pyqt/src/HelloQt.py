import sys
import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic

#실행 위치와 상관없이 동작하도록 현재 Python 파일의 위치(__file__)를 기준으로 .ui 파일 경로만듬
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_DIR,"HelloQt.ui")

from_class=uic.loadUiType(UI_PATH)[0]

class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Hello, PyQt!")


if __name__=="__main__":
    app=QApplication(sys.argv)
    myWindows=WindowClass()
    myWindows.show()
    sys.exit(app.exec())