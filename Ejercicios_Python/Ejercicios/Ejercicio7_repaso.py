from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        boton = QPushButton("Pulsa")

        self.setFixedSize(QSize(400,300))
    
        self.setCentralWidget(boton)

        boton.clicked.connect(self.botonPulsadoYSoltado)

        boton.pressed.connect(self.botonPulsado)

        boton.released.connect(self.botonSoltado)


    def botonPulsadoYSoltado(self):
        print("Boton pulsado y soltado")

    def botonSoltado(self):
        print("Boton soltado")

    def botonPulsado(self):
        print("Boton pulsado")



app = QApplication([])

window = MainWindow()

window.show()

app.exec()