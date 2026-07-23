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

        self.pixmap=QtGui.QPixmap(self.label.width(),self.label.height())
        self.pixmap.fill(Qt.GlobalColor.white)

        self.label.setPixmap(self.pixmap)
        #self.drawLine()
        self.drawGraphics()

    def drawGraphics(self):
        canvas=self.label.pixmap()
        painter=QtGui.QPainter(canvas)

        #점 그리기
        self.pen=QPen(Qt.GlobalColor.red,20,Qt.PenStyle.SolidLine)
        painter.setPen(self.pen)
        painter.drawPoint(100,100)

        #사각형 그리기
        painter.setPen(QPen(Qt.GlobalColor.blue,10,Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.black))
        painter.drawRect(150,100,100,100)

        #원 그리기
        self.pen.setBrush(Qt.GlobalColor.yellow)
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.PenStyle.SolidLine)
        painter.setPen(self.pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawEllipse(300,100,60,60)

        painter.end()


        self.label.setPixmap(canvas)
    def drawLine(self):
        canvas=self.label.pixmap()
        painter=QtGui.QPainter(canvas)

        self.pen=QPen(Qt.GlobalColor.red,5,Qt.PenStyle.SolidLine)
        painter.setPen(self.pen)
        painter.drawLine(100,100,500,100)
        
        self.pen.setBrush(Qt.GlobalColor.blue)
        self.pen.setWidth(10)
        self.pen.setStyle(Qt.PenStyle.DashDotLine)
        painter.setPen(self.pen)
        self.line=QLine(100,200,500,200)
        painter.drawLine(self.line)

        painter.setPen(QPen(Qt.GlobalColor.black,20,Qt.PenStyle.DotLine))
        self.p1=QPoint(100,300)
        self.p2=QPoint(500,300)
        painter.drawLine(self.p1,self.p2)

        painter.end()
        self.label.setPixmap(canvas)
if __name__=="__main__":

    app=QApplication(sys.argv)
    mywindows=windowClass()
    mywindows.show()
    sys.exit(app.exec())