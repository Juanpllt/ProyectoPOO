import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon
sys.path.append("../")
from logica.controladores.ControladorUsuarios import ControladorUsuarios
from menuOpcionesUsuario import MenuOpcionesUsuario
from menuOpcionesAdmin import MenuOpcionesAdmin
from Registro import Registro
from logica.clasesPrincipales.UsuarioAdmin import UsuarioAdmin
from logica.clasesPrincipales.UsuarioFinal import Usuario


class InicioSesion(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("inicioSesion.ui", self)
        self.registrarsebtn.clicked.connect(self.registrarse)
        self.ingresarbtn.clicked.connect(self.iniciarSesion)
        self.controlador = ControladorUsuarios()
    def registrarse(self):
        self.registro = Registro()
        self.registro.show()
    
    def iniciarSesion(self):
        consulta = self.controlador.iniciarSesion(self.nombreUsuariotxt.text(), self.contrasenatxt.text())
        if type(consulta) == Usuario:
            print(consulta)
            self.menu = MenuOpcionesUsuario(consulta)
            self.menu.show()
        elif type(consulta) == UsuarioAdmin:
            self.menu = MenuOpcionesAdmin(consulta)
            self.menu.show()
    