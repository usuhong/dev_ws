import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import *
from PyQt6 import QtGui

BASE_PATH=os.path.dirname(os.path.abspath(__file__))
UI_PATH=os.path.join(BASE_PATH,'paint.ui')

from_class=uic.loadUiType(UI_PATH)[0]


class windowClass(QMainWindow,from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle('mosuedrawing')
        
        self.pixmap=QtGui.QPixmap(self.label.width(),self.label.height())
        self.pixmap.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.pixmap)
        self.x,self.y=None,None
    
    def mouseMoveEvent(self, e):
        
        if self.x is None:
            self.x=e.position().x()
            self.y=e.position().y()
            return

        else:
            canvas=self.label.pixmap()
            painter=QPainter(canvas)

            self.pen=QPen(Qt.GlobalColor.black,5,Qt.PenStyle.SolidLine)
            painter.setPen(self.pen)
            painter.drawLine(int(e.position().x()-self.label.x()),int(e.position().y()-self.label.y()),int(self.x-self.label.x()),int(self.y-self.label.y()))
            painter.end()
            self.label.setPixmap(canvas)
            self.update()

            self.x=e.position().x()
            self.y=e.position().y()
    
    def mouseReleaseEvent(self, e):
        self.x=None
        self.y=None



if __name__=="__main__":

    app=QApplication(sys.argv)
    mywindows=windowClass()
    mywindows.show()
    sys.exit(app.exec())