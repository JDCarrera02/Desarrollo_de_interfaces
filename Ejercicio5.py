from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        boton = QPushButton("Pulsa")
        boton.setCheckable(True)
        boton.clicked.connect(self.botonPulsado)

        boton.clicked.connect(self.saberEstado)

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(boton)


    def botonPulsado(self):
        print("Boton pulsado")

app = QApplication([])

window = MainWindow()

window.show()

app.exec()