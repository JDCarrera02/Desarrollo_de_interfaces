from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        boton = QPushButton("Pulsa")

        self.setFixedSize(QSize(400,300))
    
        self.setCentralWidget(boton)

        self.numVeces = 0

        boton.clicked.connect(self.contarVecesPulsado)


    def botonPulsadoYSoltado(self):
        print("Boton pulsado y soltado")

    def contarVecesPulsado(self):
        self.numVeces = self.numVeces+1
        print(f'Veces que presionaste el boton {self.numVeces}')


app = QApplication([])

window = MainWindow()

window.show()

app.exec()