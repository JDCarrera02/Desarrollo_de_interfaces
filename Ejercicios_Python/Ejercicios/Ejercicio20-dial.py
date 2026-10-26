from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QDial
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("Mi aplicacion")     

        dial = QDial()

        dial.setRange(0,10)
        dial.setNotchesVisible(True)

        dial.valueChanged.connect(self.valorCambiado)
  
        self.setCentralWidget(dial)


    def valorCambiado(self, valor):
        print(valor)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()