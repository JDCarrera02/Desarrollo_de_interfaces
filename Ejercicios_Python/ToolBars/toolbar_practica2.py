from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QToolBar, QStatusBar

from PyQt6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):

    def __init__(self): 

        super().__init__()

        self.setFixedSize(QSize(500, 500))

        # Definicion de la barra de herramientas
        barra = QToolBar("Barra de herramientas")
        barra.setIconSize(QSize(16,16))

        self.addToolBar(barra)

        barra.addSeparator()

        # Añadiendo iconos a la barra de tareas
        guardar = QAction(QIcon("icons/disk.png"), "Guardar", self)
        guardar.setStatusTip("Guardar archivo")

        archivo_icono = QAction(QIcon("icons/document.png"), "Nuevo" ,self)
        archivo_icono.setStatusTip("Nuevo archivo")

        dock_icono = QAction(QIcon("icons/application-dock.png"), "Abrir", self)
        dock_icono.setStatusTip("Abrir archivo")

        # Añadir elementos a la barra de herramientas
        barra.addAction(guardar)
        barra.addAction(archivo_icono)
        barra.addAction(dock_icono)
        
        menu = self.menuBar()

        # Añadir funcinalidad en el menu
        menu_archivo = menu.addMenu("&Archivo")

        # Añadir elementos en el menu de archivo
        menu_archivo.addAction(guardar)
        menu_archivo.addAction(archivo_icono)
        menu_archivo.addAction(dock_icono)

        # Añadir menu al menu de ayuda
        menu_ayuda = menu.addMenu("&Ayuda")

        # Crear otro menu dentro del menu de ayuda
        menu_siguenos = menu_ayuda.addMenu("Siguenos")

        # Crear elementos al nuevo menu
        accion_x = QAction("X", self)
        accion_x .setStatusTip("Siguenos en X")

        accion_instagram = QAction("Instagram", self)
        accion_instagram .setStatusTip("Siguenos en instagram")

        # Añadir elementos creados al menu "siguenos"
        menu_siguenos.addAction(accion_x)
        menu_siguenos.addAction(accion_instagram)
        
        self.setStatusBar(QStatusBar(self))

app = QApplication([])

window = MainWindow()

window.show()

app.exec()