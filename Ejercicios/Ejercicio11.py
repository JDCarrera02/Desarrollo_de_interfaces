from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        self.setFixedSize(QSize(400,300))

        label = QLabel()
        input = QLineEdit()

        # Crear una señal para el input
        input.textChanged.connect(label.setText)

        layout = QVBoxLayout() # Creando la vista de tipo QVBoxLayout
        layout.addWidget(input) # Añadir los widgets (label y input)
        layout.addWidget(label)


        contenedor = QWidget()
        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)
    


app = QApplication([])

window = MainWindow()

window.show()

app.exec()