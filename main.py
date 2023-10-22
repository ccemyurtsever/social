import sys,sizing,random,time,database,messagebox,style
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QLabel, QPushButton,  QToolBar , QStatusBar, QMenuBar
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPalette, QColor,QAction
from BlurWindow.blurWindow import GlobalBlur


class mainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainPage,self).__init__()
        self.setWindowTitle("Swedish Pocketknife V1.0")
        self.setWindowIcon(QtGui.QIcon('static/icon.ico'))
   
        GlobalBlur(self.winId(),Dark=True,QWidget=self)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # No title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Transparent Background
        self.setWindowOpacity(0.8)




        
        toolbar = QToolBar("My main toolbar")
        toolbar.setStyleSheet(style.toolbarStyle)
        self.addToolBar(toolbar)

        """
        button_action = QAction("Account", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.showInfo)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        Manuel add button
        """
        def createToolButton(name,status,event):
            toolbarButton = QAction(name,self)
            toolbarButton.setStatusTip(status)
            toolbarButton.triggered.connect(event)
            toolbarButton.setCheckable(True)
            toolbar.addAction(toolbarButton)
        
        createToolButton(" File ","This is your button",self.showInfo)
        createToolButton("Account","This is your button",self.showInfo)
        createToolButton(" File ","This is your button",self.showInfo)








        infoButtonStyle = """
                color: white;
                background-color: red;
                selection-color: white;
                selection-background-color: white;
            """
        self.info = QPushButton(text=" ? ", parent=self)
        self.info.setFixedSize(70, 32)
        self.info.move(sizing.infox,sizing.infoy)
        self.info.setStyleSheet(infoButtonStyle)
        self.info.clicked.connect(self.showInfo)




        # self.text = QtWidgets.QLabel("Hello World",
                                    #  alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)


    @QtCore.Slot()
    def showInfo(self):
        time.sleep(0.1)
        messagebox.showinfo('İNFO', 'For detailed information about usage: https://github.com/ccemyurtsever/swedishPocketknife\nor contact with me:\ncemyurtsever.dev')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainPage()
    widget.resize(sizing.xdef, sizing.ydef)
    widget.move(sizing.xdefmov,sizing.ydefmove)
    widget.show()
    sys.exit(app.exec())