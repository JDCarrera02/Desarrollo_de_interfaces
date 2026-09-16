from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        self.boton = QPushButton("Pulsa")

        self.setFixedSize(QSize(400,300))
    
        self.setCentralWidget(self.boton)

        self.boton.setCheckable(True)

        self.boton.clicked.connect(self.botonPulsadoYSoltado)


    def botonPulsadoYSoltado(self, pulsado):

        self.boton.setText(["No pulsado", "Pulsado"][pulsado])   
    
        




app = QApplication([])

window = MainWindow()

window.show()

app.exec()