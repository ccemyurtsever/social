from PySide6.QtWidgets import (QMessageBox)
def message():
    msgBox = QMessageBox()
    msgBox.setText("The document has been modified.")
    msgBox.setInformativeText("Do you want to save your changes?")
    msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Save)
    ret = msgBox.exec()

# İleride messagebox bununla QMessageBox ile değiştir.