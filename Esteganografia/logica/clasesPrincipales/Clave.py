import cryptography 
from cryptography.fernet import Fernet
from typing import Any

class Clave:
    _clave : Any = 0
    
    def crearClave(self):
        self.clave = Fernet.generate_key().decode()
        print(self.clave)
    @property
    def clave(self):
        return self._clave
    
    @clave.setter
    def clave(self, clave):
        self._clave = clave
        