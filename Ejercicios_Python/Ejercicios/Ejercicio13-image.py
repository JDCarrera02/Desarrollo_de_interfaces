from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Mi aplicacion")

        label = QLabel()
        label.setPixmap(QPixmap("img/ps_logo.png"))
        label.setScaledContents(True)


        self.setCentralWidget(label)




    


app = QApplication([])

window = MainWindow()

window.show()

app.exec()