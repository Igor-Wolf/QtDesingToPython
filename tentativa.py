import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("teste.ui", self) #NOME DO ARQUIVO .ui para ser convertido dinamicamente

        self.pushButton.clicked.connect(self.clickhandler)
        
    def clickhandler(self):
        print("hello world")

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()