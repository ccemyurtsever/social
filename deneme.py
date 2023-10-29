import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit ile Metin Girişi")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # QLineEdit öğesi oluşturun
        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("Metin girin...")

        # QPushButton (buton) oluşturun
        button = QPushButton("Mesajı Göster", self)
        button.clicked.connect(self.show_message)

        layout.addWidget(self.entry)
        layout.addWidget(button)

        central_widget.setLayout(layout)

    def show_message(self):
        text = self.entry.text()
        print(f"Girilen metin: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
