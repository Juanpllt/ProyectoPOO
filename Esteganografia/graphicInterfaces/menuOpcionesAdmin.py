import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon
sys.path.append("../")
from logica.controladores.ControladorUsuarios import ControladorUsuarios
from cifro import Cifro
from descifrar import descifrar

class MenuOpcionesAdmin(QMainWindow):
    
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__()
        uic.loadUi("menuOpcionesAdmin.ui", self)
        self.cifrarbtn.clicked.connect(self.cifrar)
        self.descifrarbtn.clicked.connect(self.desCifrar)
        self.verUsuariosbtn.clicked.connect(self.verUsuarios)
        self.verUsoSoftwarebtn.clicked.connect(self.verUsoSoftware)
    def cifrar(self):
        self.cifro = Cifro(self.usuario)
        print("cifrando...")
        self.cifro.show()
    
    def desCifrar(self):
        self.descifrar = descifrar(self.usuario)
        print("descifrando...")
        self.descifrar.show()
        
    def verEsteganografia(self):
        esteganografia = ControladorUsuarios().consultarEsteganografia()
    
    def verUsuarios(self):
        usuarios = ControladorUsuarios().consultarUsuarios()
        
    
    def verUsoSoftware(self):
        uso = ControladorUsuarios().consultarUsoSoftware()