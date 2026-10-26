from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QToolBar, QStatusBar

from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        etiqueta = QLabel("Hola")

        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(etiqueta)

        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(16,16))

        self.addToolBar(barra)

        boton = QAction(QIcon("icons/brain.png"),"Mi boton", self)
        boton.setStatusTip("Este es mi boton")
        boton.triggered.connect(self.botonPulsado)

        barra.addAction(boton)
        barra.addSeparator()

        boton2 = QAction(QIcon("icons/building.png"), "Boton 2", self)
        boton2.setStatusTip("Este es mi boton 2")
        boton2.triggered.connect(self.botonPulsado)
        barra.addAction(boton2)

        barra.addSeparator()
        barra.addSeparator()

        barra.addWidget(QLabel("Texto"))
        barra.addSeparator()
        barra.addSeparator()
        barra.addWidget(QCheckBox("Seleccion"))


        self.setStatusBar(QStatusBar(self))


    def botonPulsado(self, s):
        print("Buenas",s)
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()