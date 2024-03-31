from cryptography.fernet import Fernet


class Clave:
    def __init__(self) -> None:
        pass
    def cambiarClave(self):
        clave = Fernet.generate_key()
        
    def verClave(self):
        pass
        