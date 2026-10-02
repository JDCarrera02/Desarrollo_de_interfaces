from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QTabWidget, QTextEdit, QLabel, QCheckBox

from cuadrado import Color

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()

        tabs.setTabPosition(QTabWidget.TabPosition.North)

        tabs.setMovable(True)

        # Contenido pestaña 1
        contenedor = QHBoxLayout()

        contenedor.addWidget(QLabel("Hola"))
        linea = QTextEdit()
        linea.setFixedHeight(35)
        contenedor.addWidget(linea)


        widget1 = QWidget()

        widget1.setLayout(contenedor)

        # Contenedor pestaña 2
        contenedor2 = QVBoxLayout()

        # Añadir contenido
        contenedor2.addWidget(QCheckBox("Seleccion"))
        contenedor2.addWidget(QPushButton("Pulsa"))

        widget2 = QWidget()

        widget2.setLayout(contenedor2)

        # Añadir contenedores a cada pestaña
        tabs.addTab(widget1, "pestana 1")
        tabs.addTab(widget2, "pestana 2")

        
        self.setCentralWidget(tabs)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()