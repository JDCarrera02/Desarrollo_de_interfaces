from PyQt6.QtWidgets import QApplication, QComboBox, QDateEdit, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QGridLayout, QMessageBox, QPushButton, QRadioButton, QStackedLayout, QTextEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):

    def __init__(self): 
        super().__init__()
        self.setWindowTitle("My App")

        # Para el contenido
        contenedorElementos = QVBoxLayout()

        # Para los radioButton
        contenedorButtons = QHBoxLayout()

        # Botones
        self.aragon = QRadioButton("Aragon")
        self.comVal = QRadioButton("Comunidad Valenciana")

        # Añadirlos al layout
        contenedorButtons.addWidget(self.aragon)
        contenedorButtons.addWidget(self.comVal)

        contenedorElementos.addLayout(contenedorButtons)

        # Lista deplegable
        self.desplegable = QComboBox()

        # Añadir lista desplegable
        contenedorElementos.addWidget(self.desplegable)

        # Eventos
        self.aragon.toggled.connect(self.elementosAragon)
        self.comVal.toggled.connect(self.elementosComVal)

        widget = QWidget()

        widget.setLayout(contenedorElementos)

        self.setCentralWidget(widget)

    def elementosAragon(self):
        self.desplegable.clear()
        self.desplegable.addItems(["Huesca", "Zaragoza", "Teruel"])

    def elementosComVal(self):
        self.desplegable.clear()
        self.desplegable.addItems(["Castellon", "Valencia", "Alicante"])

app = QApplication([])

window = MainWindow()

window.show()

app.exec()