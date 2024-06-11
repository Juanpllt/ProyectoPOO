import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import *
sys.path.append("../")
from logica.controladores.ControladorUsuarios import ControladorUsuarios
from logica.controladores.ControladorEsteganografia import ControladorEsteganografia 

class descifrar(QMainWindow):
    imagen = ""
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__()
        uic.loadUi("descifrar.ui", self)
        self.descifrarbtn.clicked.connect(self.descifrar)
        self.imagenbtn.clicked.connect(self.tomarImagen)
        
    def descifrar(self):
        self.controladorEstanografia = ControladorEsteganografia(self.usuario.id)
        mensaje = self.controladorEstanografia.descifrar(self.imagen)
        self.textotxt.setText(mensaje)
    
    def tomarImagen(self):
        options = QtWidgets.QFileDialog.Options()
        imagePath, _= QtWidgets.QFileDialog.getOpenFileName(None, options=options)
        
        if imagePath:
            self.imagen = imagePath
            #pixmap = QPixmap(imagePath)
            #pixmap = pixmap.scaled(600, 350)
            #self.imagenlbl.setPixmap(QPixmap(pixmap))