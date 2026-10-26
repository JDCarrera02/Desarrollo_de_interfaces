import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPushButton, QDialog, QVBoxLayout, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.etiqueta = QLabel("Pulsa aquí")
        self.setCentralWidget(self.etiqueta)

    def mouseMoveEvent(self, e):
        self.etiqueta.setText("El raton se ha movido")

    def mousePressEvent(self, e):
        self.etiqueta.setText("Se ha pulsado")

    def mouseReleaseEvent(self, e):
        self.etiqueta.setText("Maricon")

    def mouseDoubleClickEvent(self, e):
        self.etiqueta.setText("Se ha pulsado dos veces")
        

app = QApplication([])

window = MainWindow()

window.show()

app.exec()

