from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        self.botonPulsado = True

        boton = QPushButton("Pulsa")
        boton.setCheckable(True)
        boton.clicked.connect(self.botonActivado)

        boton.setChecked(self.botonPulsado)

        self.setFixedSize(QSize(400,300))

        self.setCentralWidget(boton)


    def botonActivado(self, checked):
        self.botonPulsado = checked
        print(self.botonPulsado)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()