from form4 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()


app = QApplication([])

app.setStyle("Fusion")

paleta = QPalette()

paleta = QPalette()

paleta.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))

paleta.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)

paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127))

paleta.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))

paleta.setColor(QPalette.ColorRole.AlternateBase, QColor(66, 66, 66))

paleta.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)

paleta.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)

paleta.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)

paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))

paleta.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))

paleta.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))

paleta.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))

paleta.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)

paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))

paleta.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)

paleta.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))

paleta.setColor(QPalette.ColorRole.Highlight, QColor(42, 130,218))

paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80))

paleta.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)

paleta.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))

app.setPalette(paleta)

ventana = MainWindow()

app.exec()