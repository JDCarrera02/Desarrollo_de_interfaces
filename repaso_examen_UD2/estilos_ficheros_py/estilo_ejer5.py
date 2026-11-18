import sys
from pathlib import Path

# Raíz del proyecto = carpeta padre de estilos_ficheros_py
RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))


from ficheros_py.ejercicio5_calculadora import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        # Para hacer las operaciones
        self.num1 = 0
        self.num2 = 0
        self.numtotal = 0

        # funciones

        self.pushButton_5.clicked.connect(lambda : self.label.setText(f"{self.label.text()}1"))
        self.pushButton_6.clicked.connect(lambda : self.label.setText(f"{self.label.text()}2"))
        self.pushButton_7.clicked.connect(lambda : self.label.setText(f"{self.label.text()}3"))
        self.pushButton_8.clicked.connect(lambda : self.label.setText(f"{self.label.text()}4"))
        self.pushButton_9.clicked.connect(lambda : self.label.setText(f"{self.label.text()}5"))
        self.pushButton_10.clicked.connect(lambda : self.label.setText(f"{self.label.text()}6"))
        self.pushButton_11.clicked.connect(lambda : self.label.setText(f"{self.label.text()}7"))
        self.pushButton_12.clicked.connect(lambda : self.label.setText(f"{self.label.text()}8"))
        self.pushButton_13.clicked.connect(lambda : self.label.setText(f"{self.label.text()}9"))
        self.pushButton_3.clicked.connect(lambda : self.label.setText(f"{self.label.text()}0"))
        self.pushButton_2.clicked.connect(self.funcionnumero1)
        self.pushButton_4.clicked.connect(self.funcionSuma)

        self.pushButton.clicked.connect(lambda : self.label.setText(""))

    def funcionnumero1 (self):
        self.num1  = self.label.text()
        self.label.setText("")


    def funcionSuma (self):
        
        self.num2 = self.label.text()
        self.numtotal = int(self.num1) + int(self.num2)
        self.label.setText(str(self.numtotal))


app = QApplication([])
app.setStyle("Fusion")
with open(RAIZ/"styles"/"sheet_ejer5.qss","r") as f:
    app.setStyleSheet(f.read())

ventana = MainWindow()

app.exec()
