from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")    

        self.texto = QLineEdit()

        self.texto.setMaxLength(10)
        self.texto.setPlaceholderText("Ingresa tu nombre")

        # texto.textChanged.connect(self.textoCambiado)
        self.texto.returnPressed.connect(self.introPulsado)
        
        self.setCentralWidget(self.texto)


    """def textoCambiado(self, nombre):
        print(nombre)"""

    def introPulsado(self):
        print("Intro pulsado")
        
        print(self.texto.text())


app = QApplication([])

window = MainWindow()

window.show()

app.exec()