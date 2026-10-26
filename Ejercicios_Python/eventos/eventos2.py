import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QMessageBox, QPushButton, QDialog, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):

    def __init__(self):
        
        super().__init__()
            
        self.setWindowTitle("My App")

    def contextMenuEvent(self, e):

        menuC = QMenu(self)

        menuC.addAction(QAction("Accion 1", self))
        menuC.addAction(QAction("Accion 2", self))
        menuC.addAction(QAction("Accion 3", self))

        menuC.exec(e.globalPos())

        

app = QApplication([])

window = MainWindow()

window.show()

app.exec()