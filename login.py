import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
from PyQt6.QtCore import Qt 

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Ekranı")
        self.setGeometry(100, 100, 200, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label_username = QLabel("Kullanıcı Adı:")
        layout.addWidget(label_username)

        self.input_username = QLineEdit()
        layout.addWidget(self.input_username)

        label_password = QLabel("Şifre:")
        layout.addWidget(label_password)

        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.input_password)

        login_button = QPushButton("Giriş Yap")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button)

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        # Örnek olarak sadece ekrana yazdırıyorum:
        print(f"Giriş yapıldı!\nKullanıcı Adı: {username}\nŞifre: {password}")


def run():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
