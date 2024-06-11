import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import *
sys.path.append("../")
from logica.controladores.ControladorUsuarios import ControladorUsuarios
from logica.controladores.ControladorEsteganografia import ControladorEsteganografia 

class Cifro(QMainWindow):
    imagen = ""
    def __init__(self, usuario):
        self.usuario = usuario
        super().__init__()
        uic.loadUi("cifrar.ui", self)
        self.cifrarbtn.clicked.connect(self.cifrar)
        self.imagenbtn.clicked.connect(self.tomarImagen)
        
    def cifrar(self):
        self.controladorEstanografia = ControladorEsteganografia(self.usuario.id)
        self.controladorEstanografia.cifrar(self.textotxt.toPlainText(), self.imagen)
    
    def quitarTexto(self):
        self.textotxt.setText("")
    
    def tomarImagen(self):
        options = QtWidgets.QFileDialog.Options()
        imagePath, _= QtWidgets.QFileDialog.getOpenFileName(None, options=options)
        
        if imagePath:
            self.imagen = imagePath
            pixmap = QPixmap(imagePath)
            pixmap = pixmap.scaled(600, 350)
            self.imagenlbl.setPixmap(QPixmap(pixmap))