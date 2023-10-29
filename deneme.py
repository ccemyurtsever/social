import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton

class FrameWithButton(QMainWindow):
    def __init__(self):
        super().__init()

        self.setWindowTitle("QFrame ve QPushButton Örneği")
        self.setGeometry(100, 100, 400, 300)

        main_frame = QFrame(self)
        main_frame.setGeometry(50, 50, 300, 200)
        main_frame.setFrameShape(QFrame.StyledPanel)
        main_frame.setFrameShadow(QFrame.Sunken)
        main_frame.setStyleSheet("background-color: lightblue;")

        # QFrame içine bir QPushButton ekleyin
        button = QPushButton("Tıkla", main_frame)
        button.setGeometry(100, 100, 100, 50)  # Butonun boyut ve konumunu ayarlayın

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrameWithButton()
    window.show()
    sys.exit(app.exec_())
