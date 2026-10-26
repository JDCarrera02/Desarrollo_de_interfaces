from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar

from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        etiqueta = QLabel("Hola")

        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(etiqueta)

        barra = QToolBar("Barra de herramientas")

        self.addToolBar(barra)

        boton = QAction("Mi boton", self)
        boton.setStatusTip("Este es mi boton")
        boton.triggered.connect(self.botonPulsado)

        barra.addAction(boton)

        self.setStatusBar(QStatusBar(self))


    def botonPulsado(self, s):
        print("Buenas",s)
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()