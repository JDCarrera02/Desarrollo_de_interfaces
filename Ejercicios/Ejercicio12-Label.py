from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        self.setFixedSize(QSize(400,300))

        label = QLabel("Etiqueta1: ")
        formato = label.font()
        formato.setPointSize(30)
        formato.setFamily("Times New Roman")
        formato.setBold(True)
        label.setFont(formato)

        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.setCentralWidget(label)

        """contenedor = QWidget()

        contenedor.setLayout(layout)

        self.setCentralWidget(contenedor)"""


    


app = QApplication([])

window = MainWindow()

window.show()

app.exec()