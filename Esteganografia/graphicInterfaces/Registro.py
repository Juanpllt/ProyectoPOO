import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon
sys.path.append("../")
from logica.controladores.ControladorUsuarios import ControladorUsuarios

class Registro(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("registro.ui", self)
        self.registrarsebtn.clicked.connect(self.registrarse)
    def registrarse(self):
        print(self.codigotxt.text())
        ControladorUsuarios().registrarUsuario(self.codigotxt.text(), self.nombretxt.text(), self.correotxt.text(), self.nombreUsuariotxt.text(), contrasena=self.contrasenatxt.text(), documento=self.documentotxt.text())
        
    