from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QStackedLayout

from cuadrado import Color

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("My App")

        # Contenedor principal
        plantilla1 = QVBoxLayout()

        # Contenedor botones
        contenedorBotones = QHBoxLayout()

        # Botones
        btn1 = QPushButton("red")
        btn2 = QPushButton("green")
        btn3 = QPushButton("yellow")

        contenedorBotones.addWidget(btn1)
        contenedorBotones.addWidget(btn2)
        contenedorBotones.addWidget(btn3)

        # Crear StackedLayout
        colores = QStackedLayout()

        colores.addWidget(Color("red"))
        colores.addWidget(Color("green"))
        colores.addWidget(Color("yellow"))

        # Añadir contenedores al layout principal
        plantilla1.addLayout(contenedorBotones)
        plantilla1.addLayout(colores)
        plantilla1.addSpacing(2)

        # Eventos
        btn1.clicked.connect(lambda: colores.setCurrentIndex(0))
        btn2.clicked.connect(lambda: colores.setCurrentIndex(1))
        btn3.clicked.connect(lambda: colores.setCurrentIndex(2))

        widget = QWidget()
        
        widget.setLayout(plantilla1)
        
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()