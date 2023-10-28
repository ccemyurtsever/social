from PySide6.QtWidgets import QApplication, QWidget, QLineEdit
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def createEntry(name, movex, movey, resizex, resizey, text):
        name = QLineEdit()
        name.move(movex, movey)
        name.resize(resizex, resizey)
        name.setText(text)
        name.setObjectName(name)  # 'name' değerini bir nesne adı olarak sakla
    createEntry("sss",50,50,50,50,"scads")

    def yazdir(self):
        if hasattr(self, 'name'):
            print("Name değeri:", self.name.objectName())  # 'name' değerine eriş
        else:
            print("Buton bulunamadı!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
