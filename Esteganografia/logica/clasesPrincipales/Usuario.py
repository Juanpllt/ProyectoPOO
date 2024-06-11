import abc
from abc import ABC

class Usuario(ABC):
    
    def __init__(self,id,  nombreUsuario, nombre, contrasena, correo, documento, rol):
        self.id = id
        self._nombreUsuario = nombreUsuario
        self._nombre = nombre
        self._contrasena = contrasena
        self._correo = correo
        self._documento = documento
        self._rol = rol
    
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def rol(self):
        return self._rol
    @rol.setter
    def rol(self, rol):
        self._rol = rol
    
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