import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from InicioSesion import InicioSesion
from Registro import Registro

class Inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("inicio.ui", self)
        self.iniciarSesionbtn.clicked.connect(self.iniciarSesion)
        self.registrarsebtn.clicked.connect(self.registrase)

    def iniciarSesion(self):
        
        self.inicioSesion = InicioSesion()  # Keep reference to avoid garbage collection
        self.inicioSesion.show()
    def registrase(self):
        
        self.registro = Registro()
        self.registro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    inicio = Inicio()
    inicio.show()
    sys.exit(app.exec_())
