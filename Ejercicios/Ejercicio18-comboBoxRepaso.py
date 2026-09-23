from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Mi aplicacion")    
        casilla = QCheckBox("Casilla de verificacion")  
        formato = casilla.font()
        formato.setBold(True)
        casilla.setFont(formato)    
        casilla.stateChanged.connect(self.estado)    
        self.setCentralWidget(casilla)


    def estado(self, pulsado):
        print(["No seleccionado", "Parcial", "Seleccionado"][pulsado])


app = QApplication([])

window = MainWindow()

window.show()

app.exec()