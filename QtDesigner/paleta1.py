from form4 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


app = QApplication([])

app.setStyle("Fusion")

paleta = QPalette()

paleta.setColor(QPalette.ColorRole.Window, QColor("#B0FFD9"))

paleta.setColor(QPalette.ColorRole.WindowText, QColor("#000000"))

paleta.setColor(QPalette.ColorRole.Button, QColor("#DA2121"))

app.setPalette(paleta)

ventana = MainWindow()

app.exec()