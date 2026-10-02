from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

from cuadrado import Color

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("My App")

        plantilla = QGridLayout()

        plantilla.addWidget(Color("red"),0,0) # (Fila,Columna)
        plantilla.addWidget(Color("green"),0,1)
        plantilla.addWidget(Color("yellow"),1,2)
        plantilla.addWidget(Color("blue"),2,0)


        widget = QWidget()
        
        widget.setLayout(plantilla)
        
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()