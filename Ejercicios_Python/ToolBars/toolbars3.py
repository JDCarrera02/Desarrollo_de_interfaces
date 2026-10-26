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

        menu = self.menuBar()

        menu_archivo = menu.addMenu("&Archivo")
        menu_editar = menu.addMenu("&Editar")
        menu_insertar = menu.addMenu("Insertar")

        menu_archivo.addAction(boton)
        menu_archivo.addAction(boton2)

        menu_archivo.addSeparator()

        #  Añadiendo un menu dentro de otro menu, en este caso añadiendo un menu en "menu_archivo"
        menu_mas = menu_archivo.addMenu("Mas")

        menu_mas.addAction(boton)
        menu_mas.addAction(boton2)
        


        self.setStatusBar(QStatusBar(self))


    def botonPulsado(self, s):
        print("Buenas",s)
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()