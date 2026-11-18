import sys
from pathlib import Path

# Raíz del proyecto = carpeta padre de estilos_ficheros_py
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


from ficheros_py.ejercicio3 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


app = QApplication([])
app.setStyle("Fusion")
with open(RAIZ/"styles"/"sheet_ejer3.qss","r") as f:
    app.setStyleSheet(f.read())

ventana = MainWindow()

app.exec()