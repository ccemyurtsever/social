import sys,sizing,random,time,database,messagebox,style,PysideMessagebox
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QApplication, QLabel,
                               QPushButton,  QToolBar,
                               QStatusBar, QMenuBar,
                               QMenu,QMessageBox)
from PySide6.QtCore import Slot, Qt ,QUrl
from PySide6.QtGui import QPalette, QColor, QAction, QIcon,QDesktopServices
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
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        """
        button_action = QAction("Account", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.showInfo)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        Manuel add tool button

        """
        
        def createToolButton(name,status,event):
            toolbarButton = QAction(name,self)
            toolbarButton.setStatusTip(status)
            toolbarButton.triggered.connect(event)
            toolbarButton.setCheckable(True)
            toolbar.addAction(toolbarButton)

        createToolButton(" File ","This is your button",self.showInfo)
        createToolButton("Account","This is your button",self.showInfo)
        createToolButton("Math","This is your button",self.showInfo)
        createToolButton("İnfo","This is your button",self.myWeb)



        def createToolDropdownMenu(menu_title, *items):
                    dropdown_menu = QMenu(self)
                    for item in items:
                        dropdown_menu.addAction(item)
                    dropdown_button = QAction(menu_title, self)
                    dropdown_button.setMenu(dropdown_menu)
                    toolbar.addAction(dropdown_button)

        createToolDropdownMenu("Social Media", "Youtube", "İnstagram", "X(Twitter)","Reddit",)


        def createButton():
            pass
             

    #     link_action = QAction("Website Shortkeys", self)
    #     link_action.setStatusTip("Visit the My website")
    #     link_action.triggered.connect(self.myWeb)

    #     toolbar.addAction(link_action)

        # def myWeb(self):
        #     QDesktopServices.openUrl(QUrl("cemyurtsever.dev"))









        # self.text = QtWidgets.QLabel("Hello World",
                                    #  alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout.addWidget(self.text)

    @QtCore.Slot()
    def myWeb(self):
        messagebox.showinfo('İNFO', 'For detailed information about usage: https://github.com/ccemyurtsever/swedishPocketknife\nor contact with me:\ncemyurtsever.dev\nAfter you turn it offYou will be redirected within 5 seconds.')
        time.sleep(5)
        QDesktopServices.openUrl(QUrl("https://www.cemyurtsever.dev"))

    @QtCore.Slot()
    def showInfo(self):
        messagebox.showinfo('İNFO', 'For detailed information about usage: https://github.com/ccemyurtsever/swedishPocketknife\nor contact with me:\ncemyurtsever.dev')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = mainPage()
    widget.resize(sizing.xdef, sizing.ydef)
    widget.move(sizing.xdefmov,sizing.ydefmove)
    widget.show()
    sys.exit(app.exec())