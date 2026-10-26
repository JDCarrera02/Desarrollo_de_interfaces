from PyQt6.QtCore import QDate, QLine, Qt
from PyQt6.QtWidgets import QApplication, QComboBox, QDateEdit, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QGridLayout, QMessageBox, QPushButton, QStackedLayout, QTextEdit, QVBoxLayout, QWidget

        
class MainWindow(QMainWindow):

    def __init__(self): 
        super().__init__()
        self.setWindowTitle("My App")
        
        # Para el label del nombre y el input
        
        contenedorElementos = QVBoxLayout()

        plantilla1 = QHBoxLayout()
        plantilla2 = QHBoxLayout()
        plantilla3 = QHBoxLayout()
        plantilla4 = QHBoxLayout()
        plantilla6 = QHBoxLayout()

        labelNombre = QLabel("Nombre: ")

        self.inputNombre = QLineEdit()

        # Añadirlos al layout horizontal 1
        plantilla1.addWidget(labelNombre)
        plantilla1.addWidget(self.inputNombre)

        # Crear otras etiquetas e inputs
        labelApellidos = QLabel("Apellidos:")
        self.inputApellidos = QLineEdit()

        # Añadirlos al layout horizontal 2
        plantilla2.addWidget(labelApellidos)
        plantilla2.addWidget(self.inputApellidos)

        # Etiqueta de fecha y calendario
        labelFecha = QLabel("Fecha de alta:")
        self.calendario = QDateEdit()
        self.calendario.setCalendarPopup(True)
        self.calendario.setMinimumDate(QDate(2006,1,1))

        plantilla3.addWidget(labelFecha)
        plantilla3.addWidget(self.calendario)

        # Etiqueta departamento y comboBox
        labelDepartamento = QLabel("Departamento: ")

        # Desplegable
        self.desplegable = QComboBox()
        self.desplegable.addItems(["Contabilidad", "Administracion", "Produccion"])

        # Añadirlos a la plantilla horizontal 4
        plantilla4.addWidget(labelDepartamento)
        plantilla4.addWidget(self.desplegable)


        # Botones
        botonGrabar = QPushButton("Enviar")
        botonReset = QPushButton("Reset")

        plantilla6.addWidget(botonGrabar)
        plantilla6.addWidget(botonReset)

        contenedorElementos.addLayout(plantilla1)
        contenedorElementos.addLayout(plantilla2)
        contenedorElementos.addLayout(plantilla3)
        contenedorElementos.addLayout(plantilla4)
        contenedorElementos.addLayout(plantilla6)

        contenedorElementos.addSpacing(4)

        # Eventos de los botones
        botonGrabar.clicked.connect(self.cuadroDialogo)
        botonReset.clicked.connect(self.resetInfo)

        widget = QWidget()
        
        widget.setLayout(contenedorElementos)
        
        self.setCentralWidget(widget)


    def resetInfo(self):
        self.inputNombre.setText("")
        self.inputApellidos.setText("")
        self.calendario.setDate(QDate(2006,1,1))
        self.desplegable.setCurrentIndex(0)
        self.textoDescripcion.setText("")

    def cuadroDialogo(self):

        nombre = self.inputNombre.text()
        apellidos = self.inputApellidos.text()

        mensaje = QMessageBox.question(
            self, 
            'Confirmation',
            f'Si eres {nombre} {apellidos} pulsa Si',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if mensaje == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            self.inputNombre.setText("")
            self.inputApellidos.setText("")






app = QApplication([])

window = MainWindow()

window.show()

app.exec()