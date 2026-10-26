import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPushButton, QDialog, QVBoxLayout, QWidget


class OtraVentana(QWidget):
    
    def __init__(self):
        
        super().__init__()

        plantilla = QVBoxLayout()
        self.etiqueta = QLabel("Otra ventana")
        plantilla.addWidget(self.etiqueta)
        self.setLayout(plantilla)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi aplicación")

        boton = QPushButton("Pulsa aquí")
        boton.clicked.connect(self.mostrarVentana)
        self.setCentralWidget(boton)


    def mostrarVentana(self):
        self.window = OtraVentana()
        self.window.show()
        


app = QApplication([])

window = MainWindow()

window.show()

app.exec()