import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.QtCore import *
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QIntValidator

import socket

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
UI_PATH=os.path.join(BASE_DIR,"TCPClient.ui")

from_class=uic.loadUiType(UI_PATH)[0]

class WindowClass(QMainWindow,from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegularExpression(
            "^" + range + "\\." + range + "\\." + range + "\\." + range + "$"
        )

        self.ipEdit.setValidator(QRegularExpressionValidator(ipRegex,self))
        self.portEdit.setValidator(QIntValidator())

        self.setWindowTitle("TCPClient")
        self.btnConnect.clicked.connect(self.connected)

    def connected(self):
        ip=self.ipEdit.text()
        port=self.portEdit.text()

        self.sock=socket.socket()
        self.sock.connect((ip,int(port)))
        self.test()
        self.sock.close()

    def test(self):
        send_message="Hello TCP!"
        self.sock.send(send_message.encode())

        recv_message=""
        while len(recv_message) < len(send_message):
            recv_message+=self.sock.recv(1).decode()

        print(recv_message)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    mywindows=WindowClass()
    mywindows.show()
    sys.exit(app.exec())