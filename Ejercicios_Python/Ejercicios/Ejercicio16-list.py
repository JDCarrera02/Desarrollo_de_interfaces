from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Mi aplicacion")    

        lista = QListWidget()

        lista.addItems(["Uno", "Dos", "Tres"])

        lista.currentTextChanged.connect(self.muestraTexto)

        lista.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.setCentralWidget(lista)


    def muestraTexto(self, texto):
        print(texto)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()