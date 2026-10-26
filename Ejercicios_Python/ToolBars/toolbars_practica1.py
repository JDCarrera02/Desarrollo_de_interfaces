from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QToolBar, QStatusBar

from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.numVeces = 0

        self.etiqueta = QLabel("Hola!")

        self.etiqueta.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setCentralWidget(self.etiqueta)

        # Definicion de la barra de herramientas
        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(16,16))

        self.addToolBar(barra)

        barra.addSeparator()

        # Añadiendo una QAction y un QIcon - conectado a una funcion
        boton = QAction(QIcon("icons/brain.png"), "Cambiar texto", self)
        boton.setStatusTip("Este es mi boton")
        boton.triggered.connect(self.cambiarTexto)

        # Añadir el elemento en la barra de herramientas
        barra.addAction(boton)
        
        menu = self.menuBar()

        # Añadir funcinalidad en el menu
        menu_archivo = menu.addMenu("&Archivo")

        # Añadir QAction al menu Archivo
        menu_archivo.addAction(boton)


        
        self.setStatusBar(QStatusBar(self))


    def cambiarTexto(self):
        self.numVeces +=1
        self.etiqueta.setText(f"Texto cambiado {self.numVeces}")
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()