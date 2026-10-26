from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        # PLnatillas identificadas 2 de organizacion vertical y una de organizacion horizontal
        plantilla1 = QVBoxLayout()
        plantilla2 = QHBoxLayout()
        plantilla3 = QVBoxLayout()

        # Cabecera (Horizontal)
        boton1 = QPushButton("Boton 1")
        boton2 = QPushButton("Boton 2")

        # Añadirlos a la plantilla 2
        plantilla2.addWidget(boton1)
        plantilla2.addWidget(boton2)

        # PLantilla 3 (Vertical) añadir boton
        boton3 = QPushButton("Boton 3")

        # Añadirlo
        plantilla3.addWidget(boton3)

        # Añadir los Layouts en la plantilla principal (Vertical)
        plantilla1.addLayout(plantilla2)
        plantilla1.addLayout(plantilla3)

        widget = QWidget()

        widget.setLayout(plantilla1)

        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()