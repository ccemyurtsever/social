import sys,sizing,random,time,database
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QLabel, QPushButton,  QToolBar , QStatusBar
from PySide6.QtCore import Slot
from PySide6.QtGui import QPalette, QColor
from BlurWindow.blurWindow import GlobalBlur


class mainPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Swedish Pocketknife V1.0")
        self.setWindowIcon(QtGui.QIcon('static/icon.ico'))
   
        GlobalBlur(self.winId(),Dark=True,QWidget=self)
        self.setStyleSheet("background-color: white;")
        self.setWindowOpacity(0.9)




        self.button = QtWidgets.QPushButton("Click me!")

        # self.text = QtWidgets.QLabel("Hello World",
                                    #  alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        time.sleep(0.2)
        print("Magic!")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainPage()
    widget.resize(sizing.xdef, sizing.ydef)
    widget.move(sizing.xdefmov,sizing.ydefmove)
    widget.show()
    
    sys.exit(app.exec())