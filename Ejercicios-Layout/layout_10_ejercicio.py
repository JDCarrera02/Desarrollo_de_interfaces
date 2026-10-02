from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QStackedLayout, QWidget

from cuadrado import Color

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("My App")

        plantilla = QStackedLayout()

        plantilla.addWidget(Color("red"))
        plantilla.addWidget(Color("green"))
        plantilla.addWidget(Color("yellow"))
        plantilla.addWidget(Color("blue"))
        plantilla.addWidget(Color("cian"))
        plantilla.addWidget(Color("purple"))
        plantilla.addWidget(Color("gray"))

        plantilla.setCurrentIndex(6)

        widget = QWidget()
        
        widget.setLayout(plantilla)
        
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()