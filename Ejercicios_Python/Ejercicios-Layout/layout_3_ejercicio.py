from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        plantilla = QVBoxLayout()
        boton1 = QPushButton("Boton1")
        boton2 = QPushButton("Boton2")
        boton3 = QPushButton("Boton3")

        plantilla.setSpacing(20)
        plantilla.setContentsMargins(10,10,10,10)
        

        # Plantilla 1
        plantilla.addWidget(boton1)
        plantilla.addWidget(boton2)
        plantilla.addWidget(boton3)

        boton1.clicked.connect(self.botonPulsado)
        boton2.clicked.connect(self.botonPulsado)
        boton3.clicked.connect(self.botonPulsado)

        widget = QWidget()

        widget.setLayout(plantilla)

        self.setCentralWidget(widget)

    def botonPulsado(self):
        # nombre = nombreBoton[len(nombreBoton)-1:]
        print(f"{self.sender().text()} pulsado")




app = QApplication([])

window = MainWindow()

window.show()

app.exec()