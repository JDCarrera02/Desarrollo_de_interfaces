from PyQt6.QtWidgets import QPushButton, QApplication, QStyle
from PyQt6.QtCore import QSize

app = QApplication([])

boton = QPushButton()

estilo = boton.style()

icono = estilo.standardIcon(QStyle.StandardPixmap.SP_MediaPlay)

boton.setIcon(icono)

boton.setIconSize(QSize(190, 190))

boton.show()

app.exec()