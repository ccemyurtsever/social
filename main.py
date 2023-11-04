import sys,sizing,random,time,database,messagebox,style,pysideMessagebox,ui_youtube
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (QApplication, QLabel,
                               QPushButton,  QToolBar,
                               QStatusBar, QMenuBar,
                               QMenu,QMessageBox,QLineEdit,
                               QVBoxLayout,QFrame)
from PySide6.QtCore import Slot, Qt ,QUrl
from PySide6.QtGui import QPalette, QColor, QAction, QIcon,QDesktopServices
from BlurWindow.blurWindow import GlobalBlur



class mainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainPage,self).__init__()
        self.setWindowTitle("Swedish Pocketknife V1.0")
        self.setWindowIcon(QtGui.QIcon('static/icon.ico'))
        # self.setStyleSheet("background-color:#333;")
   
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

        def createToolDropdownMenu(menu_title, *items):
                    dropdown_menu = QMenu(self)
                    for item in items:
                        dropdown_menu.addAction(item)
                    dropdown_button = QAction(menu_title, self)
                    dropdown_button.setMenu(dropdown_menu)
                    toolbar.addAction(dropdown_button)

        createToolDropdownMenu("Social Media", "Youtube", "İnstagram", "X (Twitter)","Reddit",)

        createToolButton("İnfo","This is your button",self.myWeb)

        """

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
        SEE YOU LATER

        """

        # self.main = QLineEdit(self)
        # self.main.move(100,100)
        # self.main.resize(60,60)
        # self.main.setText("")
        # print(self.main.displayText())
        # QLineEdit öğesi oluşturun

        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("Metin girin...")
        self.entry.move(3,100)


        QtCore.Slot()
        def yazdir():
            pass

            

        def createButton(name, text, event, resizex, resizey, movex, movey):
            button = QPushButton(text, self)
            button.clicked.connect(event)
            button.move(movex, movey)
            button.resize(resizex, resizey)
            return button

        createButton("namee", "text", self.youtubeUi, 50, 50, 300, 300)


        # def createLabel(text):
        #     label = QLabel(text)  
        # label = QLabel("CY")
        # font = label.font()
        # font.setPointSize(70)
        # label.setFont(font)
        # label.setAlignment(
        #     Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        # )
        # self.setCentralWidget(label)


        # def createFrame(movex,movey,xdef,ydef,bgColor):
        #     main_frame = QFrame(self)
        #     main_frame.setGeometry(movex, movey, xdef, ydef)
        #     main_frame.setFrameShape(QFrame.StyledPanel)  # Çerçeve şekli
        #     main_frame.setFrameShadow(QFrame.Sunken)  # Çerçeve gölgesi
        #     main_frame.setStyleSheet(f"background-color: {bgColor};")

        # createFrame(2,130,150,sizing.ydef-250,"grey")
        # createFrame(2,765,1558,100,"grey")

    def youtubeUi(self):
        import ui_youtube  # ui_youtube modülünü içe aktarın
        youtube_window = mainPage()  # Bir QMainWindow veya QWidget oluşturun
        ui = ui_youtube.Ui_Form()  # ui_youtube modülünden Ui_Form sınıfını oluşturun
        ui.setupUi(youtube_window)  # YouTube penceresini oluşturun
        youtube_window.show()
        
        


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