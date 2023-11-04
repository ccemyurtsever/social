# -*- coding: utf-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QLineEdit, QProgressBar, QPushButton, QWidget
import sys,youtube

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(380, 440)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(260, 200, 69, 22)
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(170, 200, 69, 22)

        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(70, 200, 69, 22)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(20, 150, 47, 31)
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.label.setLineWidth(1)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(70, 250, 121, 23)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(60, 310, 301, 23)
        self.progressBar.setValue(24)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(70, 149, 261, 31)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(210, 250, 121, 23)
        self.retranslateUi(Form)

        self.pushButton.clicked.connect(self.download)

    def download(self):
        if self.comboBox_3.currentText() == "mp3":
            youtube.ytMp3Download()
        elif self.comboBox_3.currentText() == "mp4":
            url = self.lineEdit.text()
            quality = self.comboBox_2.currentText()
            # fps = self.comboBox.currentText()
            youtube.ytDownload(url,quality,30)
        else:
            youtube.fastYoutube()




        print(self.lineEdit.text())
        print(self.comboBox_3.currentText())

    def retranslateUi(self, Form):
        Form.setWindowTitle("Youtube")
        self.comboBox.setItemText(0, "30 fps")
        self.comboBox.setItemText(1, "60 fps")

        self.comboBox_2.setItemText(0, "144p")
        self.comboBox_2.setItemText(1, "240p")
        self.comboBox_2.setItemText(2, "360p")
        self.comboBox_2.setItemText(3, "480p")
        self.comboBox_2.setItemText(4, "720p")
        self.comboBox_2.setItemText(5, "1080p")
        self.comboBox_2.setItemText(6, "1440p")
        self.comboBox_2.setItemText(7, "2160p")
        self.comboBox_2.setItemText(8, "4320p")

        self.comboBox_3.setItemText(0, "mp4")
        self.comboBox_3.setItemText(1, "mp3")




        self.label.setText("Url:")
        self.pushButton.setText("Download")
        self.pushButton_2.setText("Stop")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
