from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QRadioButton, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        # Plantilla principal 
        plantilla1 = QHBoxLayout()

        # Grupo de radioButtons
        radioButtons = QVBoxLayout()
        
        # Grupo de botones
        grupoBotones = QVBoxLayout()

        # Crear los grupos

        # Grupo 1 (radio Buttons)
        rButton1 = QRadioButton("Opcion 1")
        rButton2 = QRadioButton("Opcion 2")
        rButton3 = QRadioButton("Opcion 3")

        radioButtons.addWidget(rButton1)
        radioButtons.addWidget(rButton2)
        radioButtons.addWidget(rButton3)

        # Grupo 2 (Botones)
        
        boton1 = QPushButton("Opcion 1")
        boton2 = QPushButton("Opcion 2")
        boton3 = QPushButton("Opcion 3")

        # Añadirlos
        grupoBotones.addWidget(boton1)
        grupoBotones.addWidget(boton2)
        grupoBotones.addWidget(boton3)

        # Añadirlos a la plantilla principal
        plantilla1.addLayout(radioButtons)
        plantilla1.addLayout(grupoBotones)

        widget = QWidget()
    
        widget.setLayout(plantilla1)
    
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()