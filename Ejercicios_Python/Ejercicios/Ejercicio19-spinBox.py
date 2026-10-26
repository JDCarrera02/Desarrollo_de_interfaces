from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("Mi aplicacion")     

        spinBox = QSpinBox()

        spinBox.setRange(0,20)
        spinBox.setSingleStep(2)
        spinBox.setSuffix(" €")

        spinBox.valueChanged.connect(self.valorCambiado)
        spinBox.textChanged.connect(self.valorCambiado)

        self.setCentralWidget(spinBox)


    def valorCambiado(self, valor):
        print(valor)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()