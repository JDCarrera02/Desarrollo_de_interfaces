from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel

class OtraVentana(QWidget):
   
    def __init__(self): # Creación de una función
        super().__init__() # LLamo al constructor del padre

        plantilla = QVBoxLayout()
        self.etiqueta = QLabel()
        plantilla.addWidget(self.etiqueta)

        self.setLayout(plantilla)

class MainWindow(QMainWindow): # Creación de una clase
    
    def __init__(self): # Creación de una función
        super().__init__() # LLamo al constructor del padre
        
        self.window = OtraVentana()
        self.setWindowTitle("My App")

        self.boton = QPushButton("Pulsa aquí")
        self.boton.clicked.connect(self.mostrarOtraVentana)

        self.input = QLineEdit()

        # Esta etiqueta está en otra ventana 
        self.input.textChanged.connect(self.window.etiqueta.setText) 

        plantilla = QVBoxLayout()
        plantilla.addWidget(self.boton)
        plantilla.addWidget(self.input)

        contenedor = QWidget()
        contenedor.setLayout(plantilla)

        self.setCentralWidget(contenedor)

    def mostrarOtraVentana(self):
        self.window.show()
          
app = QApplication([])
window = MainWindow()
window.show()
app.exec()