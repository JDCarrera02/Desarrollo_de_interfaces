from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel, QCheckBox

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        plantilla1 = QVBoxLayout()
        plantilla2 = QHBoxLayout()
        plantilla3 = QVBoxLayout()

        # Cabecera
        # Crear el label y el QLineEdit
        
        label = QLabel("Texto")
        linea = QLineEdit()

        # Ingresar los elementos en la plantilla
        plantilla2.addWidget(label)
        plantilla2.addWidget(linea)

        # CheckBoxes
        caja1 = QCheckBox("Opcion 1")
        caja2 = QCheckBox("Opcion 2")
        caja3 = QCheckBox("Opcion 3")

        # Añadirlos a la plantilla
        plantilla3.addWidget(caja1)
        plantilla3.addWidget(caja2)
        plantilla3.addWidget(caja3)

        # Señales de las cajas
        caja1.stateChanged.connect(self.estado)
        caja2.stateChanged.connect(self.estado)
        caja3.stateChanged.connect(self.estado)

        # Añadir los Layouts en la plantilla principal
        plantilla1.addLayout(plantilla2)
        plantilla1.addLayout(plantilla3)


        widget = QWidget()

        widget.setLayout(plantilla1)

        self.setCentralWidget(widget)


    def estado(self, pulsado):
        # Mostrar que opcion ha seleccionado
        print(f"{self.sender().text()}", ["No seleccionado", " ", "Seleccionado"][pulsado])



app = QApplication([])

window = MainWindow()

window.show()

app.exec()