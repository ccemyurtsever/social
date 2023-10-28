import sys,sizing,random,time,database,messagebox,style,PysideMessagebox
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QApplication, QLabel,
                               QPushButton,  QToolBar,
                               QStatusBar, QMenuBar,
                               QMenu,QMessageBox,QLineEdit,
                               QVBoxLayout)
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

        # messagebox.showinfo('İNFO', 'For your information, only the YouTube part is currently working. https://github.com/ccemyurtsever/swedishPocketknife\nor contact with me:\ncemyurtsever.dev')
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

        def createToolDropdownMenu(menu_title, *items):
                    dropdown_menu = QMenu(self)
                    for item in items:
                        dropdown_menu.addAction(item)
                    dropdown_button = QAction(menu_title, self)
                    dropdown_button.setMenu(dropdown_menu)
                    toolbar.addAction(dropdown_button)

        createToolDropdownMenu("Social Media", "Youtube", "İnstagram", "X (Twitter)","Reddit",)

        createToolButton("İnfo","This is your button",self.myWeb)

                
        # def createEntry(self,number,movex,movey,resizex,resizey,text):
        #     while number != 0:
        #         entryName = f"Entry{number}"
        #         entryName = QLineEdit(self)
        #         entryName.move(movex,movey)
        #         entryName.resize(resizex,resizey)
        #         entryName.setText(text)
        #         number -= 1
            
        # createEntry(self,1,400,400,60,60,"deneme")

        
        # def createEntry(self,name,movex,movey,resizex,resizey,text):
        #     self.name = QLineEdit(self)
        #     self.name.move(movex,movey)
        #     self.name.resize(resizex,resizey)
        #     self.name.setText(text)
        #     print(name)

                        
        # createEntry(self,"nameess",400,400,60,60,"deneme")

        # def yazdir(self):
        #     if hasattr(createEntry, 'btn'):
        #         print("Butonun metni:", self)
        #     else:
        #         print("Buton bulunamadı!")

        def createEntry(self,name,movex,movey,resizex,resizey,text):
            self.name = QLineEdit(self)
            self.name.move(movex,movey)
            self.name.resize(resizex,resizey)
            self.name.setText(text)
            print(name)
            print(self.name.text())

                        
        createEntry(self,"nameess",400,400,60,60,"deneme")

        @QtCore.Slot()
        def yazdir(self):
            if hasattr(createEntry, 'nameess'):
                print("Entry metni:", self)
            else:
                print("Entry bulunamadı!")




        def createButton(name,text,event,resizex,resizey,movex,movey):
            self.name = QPushButton(text,self)
            self.name.clicked.connect(event)
            self.name.move(movex,movey)
            self.name.resize(resizex,resizey)
            return name
        
        createButton("namee","text",yazdir,50,50,300,300)




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