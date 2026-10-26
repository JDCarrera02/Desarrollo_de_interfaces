from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QStackedLayout, QTabWidget

from cuadrado import Color

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()

        tabs.setTabPosition(QTabWidget.TabPosition.North)

        tabs.setMovable(True)

        tabs.addTab(Color("red"), "rojo")
        tabs.addTab(Color("yellow"), "amarillo")
        tabs.addTab(Color("green"), "verde")
        tabs.addTab(Color("cyan"), "cian")
        

        
        self.setCentralWidget(tabs)


app = QApplication([])

window = MainWindow()

window.show()

app.exec()