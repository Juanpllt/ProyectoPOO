import abc
from abc import ABC

class Usuario(ABC):
    
    def __init__(self, nombreUsuario, nombre, contrasena, correo, documento):
        self._nombreUsuario = nombreUsuario
        self._nombre = nombre
        self._contrasena = contrasena
        self._correo = correo
        self._documento = documento
    
    
    @abc.abstractmethod
    def crearUsuario():
        pass
    
    @abc.abstractmethod
    def iniciarSesion(self):
        pass
    
    @abc.abstractmethod
    def recuperarContrasena(self):
        pass
    
    
    
    def verAnteriores(self):
        pass
    
    def cifrar(self):
        pass
    def esconderMensaje(self):
        pass
    def mostrarMensaje(self):
        pass
    def descifrar(self):
        pass
    def cerrarSesion(self):
        pass
    def salir(self):
        pass
    def guardarTexto(self):
        pass
    def guardarProceso(self):
        pass
    def guardarImagen(self):
        pass
    def enviarCorreo(self):
        
    
    @property
    def nombreUsuario(self):
        return self._nombreUsuario
    @nombreUsuario.setter
    def nombreUsuario(self, nombreUsuario):
        self._nombreUsuario= nombreUsuario
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre
        
    @property
    def contrasena(self):
        return self._contrasena
    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena= contrasena
    
    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self, correo):
        self._correo= correo
        
    @property
    def documento(self):
        return self._documento
    @documento.setter
    def documento(self, documento):
        self._documento= documento