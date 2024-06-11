import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon
sys.path.append("../")
from logica.controladores.ControladorUsuarios import ControladorUsuarios
from cifro import Cifro
from descifrar import descifrar

class MenuOpcionesUsuario(QMainWindow):
    
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__()
        uic.loadUi("menuOpcionesUsuario.ui", self)
        self.cifrarbtn.clicked.connect(self.cifrar)
        self.descifrarbtn.clicked.connect(self.desCifrar)
        print("hola")
    def cifrar(self):
        self.cifro = Cifro(self.usuario)
        print("hola")
        self.cifro.show()
    
    def desCifrar(self):
        self.descifrar = descifrar(self.usuario)
        print("descifrando...")
        self.descifrar.show()