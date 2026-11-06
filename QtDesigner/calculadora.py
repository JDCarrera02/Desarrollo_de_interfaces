from PyQt6.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton, QMainWindow, QLabel, QVBoxLayout

class MainWindow(QMainWindow): 

    def __init__(self):
        super().__init__()
        #Widget Principal
        widget = QWidget() #importante para mostrar la interfaz

        # Vertical y horizontal
        vertical = QVBoxLayout()
        fila1 = QHBoxLayout()
        fila2 = QHBoxLayout()
        fila3 = QHBoxLayout()
        fila4 = QHBoxLayout()
        fila5 = QHBoxLayout()
        fila6 = QHBoxLayout()


        #PushButtons
        self.boton1 = QPushButton("1")
        self.boton2 = QPushButton("2")
        self.boton3 = QPushButton("3")
        self.boton4 = QPushButton("4")
        self.boton5 = QPushButton("5")
        self.boton6 = QPushButton("6")
        self.boton7 = QPushButton("7")
        self.boton8 = QPushButton("8")
        self.boton9 = QPushButton("9")
        self.botonmas = QPushButton("+")
        self.boton0 = QPushButton("0")
        self.botonigual = QPushButton("=")
        self.botonce = QPushButton("CE")


        #Text
        self.texto1 = QLabel("")
        self.num1 = 0
        self.num2 = 0
        self.numtotal = 0
        
        # Filas
        fila1.addWidget(self.texto1)

        fila2.addWidget(self.boton7)
        fila2.addWidget(self.boton8)
        fila2.addWidget(self.boton9)

        fila3.addWidget(self.boton4)
        fila3.addWidget(self.boton5)
        fila3.addWidget(self.boton6)       

        fila4.addWidget(self.boton3)
        fila4.addWidget(self.boton2)
        fila4.addWidget(self.boton1) 
    
        fila5.addWidget(self.botonmas)
        fila5.addWidget(self.boton0)
        fila5.addWidget(self.botonigual)      

        fila6.addWidget(self.botonce)   


        vertical.addLayout(fila1)
        vertical.addLayout(fila2)
        vertical.addLayout(fila3)
        vertical.addLayout(fila4)
        vertical.addLayout(fila5)
        vertical.addLayout(fila6)


        # funciones

        self.boton1.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}1"))
        self.boton2.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}2"))
        self.boton3.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}3"))
        self.boton4.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}4"))
        self.boton5.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}5"))
        self.boton6.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}6"))
        self.boton7.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}7"))
        self.boton8.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}8"))
        self.boton9.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}9"))
        self.boton0.clicked.connect(lambda : self.texto1.setText(f"{self.texto1.text()}0"))
        self.botonmas.clicked.connect(self.funcionnumero1)
        self.botonigual.clicked.connect(self.funcionSuma)

        self.botonce.clicked.connect(lambda : self.texto1.setText(""))


        widget.setLayout(vertical)


        self.setCentralWidget(widget)
    def funcionnumero1 (self,s):
        self.num1  = self.texto1.text()
        print(self.num1)
        self.texto1.setText("")
    def funcionSuma (self,s):
        
        self.num2 = self.texto1.text()
        self.numtotal = int(self.num1) + int(self.num2)
        self.texto1.setText(str(self.numtotal))

app = QApplication([])

window = MainWindow()

window.show()

with open("estilos/estilo_calculadora.qss","r") as f:
    app.setStyleSheet(f.read())


app.exec()