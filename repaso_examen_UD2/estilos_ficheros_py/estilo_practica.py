import sys
from pathlib import Path

# Raíz del proyecto = carpeta padre de estilos_ficheros_py
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


from ficheros_py.practica_repaso import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Botones de los colores
        self.pushButton.toggled.connect(lambda : self.label_4.setStyleSheet("color: red"))
        self.pushButton_2.toggled.connect(lambda : self.label_4.setStyleSheet("color: green"))
        self.pushButton_3.toggled.connect(lambda : self.label_4.setStyleSheet("color: blue"))

        # Botones de tipo de fuente
        self.pushButton_4.toggled.connect(lambda : self.label_4.setStyleSheet("font-family: Verdana"))
        self.pushButton_5.toggled.connect(lambda : self.label_4.setStyleSheet("font-family: Arial"))
        self.pushButton_6.toggled.connect(lambda : self.label_4.setStyleSheet("font-family: Tahoma"))

        # Botones de tamaño de letra
        self.pushButton_7.toggled.connect(lambda : self.label_4.setStyleSheet("font-size: 14px"))
        self.pushButton_8.toggled.connect(lambda : self.label_4.setStyleSheet("font-size: 10px"))
        self.pushButton_9.toggled.connect(lambda : self.label_4.setStyleSheet("font-size: 12px"))



app = QApplication([])
app.setStyle("Fusion")
with open(RAIZ/"styles"/"sheet_practica_repaso.qss","r") as f:
    app.setStyleSheet(f.read())

ventana = MainWindow()

app.exec()