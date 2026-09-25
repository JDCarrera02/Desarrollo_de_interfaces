from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGroupBox, QHBoxLayout, QWidget, QCheckBox, QVBoxLayout

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        plantilla1 = QHBoxLayout()

        # Grupo de cajas
        grupoCajas = QVBoxLayout()
        

        # Grupo de cajas 2
        grupoCajas2 = QVBoxLayout()

        # Crear los grupos

        # Grupo 1
        grupo1 = QGroupBox("Botones")

        caja1 = QCheckBox("Opcion 1")
        caja2 = QCheckBox("Opcion 2")
        caja3 = QCheckBox("Opcion 3")

        grupoCajas.addWidget(caja1)
        grupoCajas.addWidget(caja2)
        grupoCajas.addWidget(caja3)

        grupo1.setLayout(grupoCajas)

        # Grupo 2
        grupo2 = QGroupBox("Botones")
        
        caja_1 = QCheckBox("Opcion 1")
        caja_2 = QCheckBox("Opcion 2")
        caja_3 = QCheckBox("Opcion 3")
        
        grupoCajas2.addWidget(caja_1)
        grupoCajas2.addWidget(caja_2)
        grupoCajas2.addWidget(caja_3)

        grupo2.setLayout(grupoCajas2)

        # Añadirlos a la plantilla principal
        plantilla1.addWidget(grupo1)
        plantilla1.addWidget(grupo2)

        widget = QWidget()
    
        widget.setLayout(plantilla1)
    
        self.setCentralWidget(widget)

app = QApplication([])

window = MainWindow()

window.show()

app.exec()