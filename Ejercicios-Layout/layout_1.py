from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget

from cuadrado import Color

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        plantilla = QHBoxLayout()

        plantilla.addWidget(Color("red"))

        plantilla.addWidget(Color("green"))

        plantilla.addWidget(Color("blue"))

        widget = QWidget()

        widget.setLayout(plantilla)

        self.setCentralWidget(widget)




app = QApplication([])

window = MainWindow()

window.show()

app.exec()